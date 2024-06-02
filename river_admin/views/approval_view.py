from typing import Tuple, List, Type

from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST
from river.models import State, TransitionMeta, Workflow
from river.models.fields.state import StateField

from river_admin.views import post
from rest_framework import serializers


class RequestDataExtractor:
    """
    Extracts the necessary parameters from the request data.
    """
    @staticmethod
    def extract(request) -> Tuple[str, int, str, str]:
        """
        Extracts content type name, object ID, destination state, and state field name from the request.

        Args:
        request: The incoming HTTP request containing the data.

        Returns:
        Tuple containing content type name, object ID, destination state, and state field name.
        """
        content_type_name = request.data.get('content_type_name')
        object_id = request.data.get('object_id')
        destination_state = request.data.get('destination_state')
        state_field_name = request.data.get('state_field_name', None)
        return content_type_name, object_id, destination_state, state_field_name


class ModelFetcher:
    """
    Fetches the model class and model instances based on the content type name and object ID.
    """
    @staticmethod
    def fetch_model_class(content_type_name: str) -> Type[Model]:
        """
        Fetches the model class from the content type name.

        Args:
        content_type_name: The name of the model class to fetch.

        Returns:
        The Django model class.
        """
        if not isinstance(content_type_name, str):
            raise ValueError('content_type_name must be a string')
        return get_object_or_404(ContentType.objects.all(), model=content_type_name).model_class()

    @staticmethod
    def fetch_workflow_object(model_class: Type[Model], object_id: int) -> Model:
        """
        Fetches the workflow object instance by its ID.

        Args:
        model_class: The class of the model to fetch.
        object_id: The primary key ID of the model instance.

        Returns:
        The model instance.
        """
        return get_object_or_404(model_class.objects.all(), pk=object_id)


class StateFieldUtil:
    """
    Utility class for handling operations related to state fields within models.
    """
    @staticmethod
    def list_state_fields(model_class: Type[Model]) -> List[str]:
        """
        Lists the state fields present in the model.

        Args:
        model_class: The model class to inspect.

        Returns:
        A list of state field names.
        """
        return [field.name for field in model_class._meta.get_fields() if isinstance(field, StateField)]

    @staticmethod
    def is_valid_state_field(model_class: Type[Model], field_name: str) -> bool:
        """
        Checks if a given field name is a valid state field for the specified model.

        Args:
        model_class: The model class to check.
        field_name: The field name to validate.

        Returns:
        True if the field is a valid state field, False otherwise.
        """
        return any(isinstance(field, StateField) and field.name == field_name for field in model_class._meta.get_fields())


class TransitionApprover:
    """
    Handles the approval process for transitions in workflow states.
    """
    @staticmethod
    def approve_all(user, workflow_object: Model, state_field_names: List[str], destination_state: str = None):
        """
        Approves transitions for all specified state fields on a given workflow object.

        Args:
        user: The user who is approving the transition.
        workflow_object: The workflow object undergoing transition.
        state_field_names: List of state field names to process for approval.
        destination_state: The destination state label to transition to, if specified.
        """
        for state_field_name in state_field_names:
            TransitionApprover.approve_for_field(user, workflow_object, state_field_name, destination_state)

    @staticmethod
    def approve_for_field(user, workflow_object: Model, state_field_name: str, destination_state: str = None):
        """
        Approves the transition for a single state field on a given workflow object.

        Args:
        user: The user who is approving the transition.
        workflow_object: The workflow object undergoing transition.
        state_field_name: The state field to process.
        destination_state: The destination state label to transition to, if specified.
        """
        river_attr = getattr(workflow_object, "river", None)
        if river_attr:
            state_field = getattr(river_attr, state_field_name, None)
            if state_field:
                destination = State.objects.get(label=destination_state) if destination_state else None
                try:
                    state_field.approve(as_user=user, next_state=destination)
                except Exception as e:
                    return Response({
                        "message": f"Error approving transition: {e}"
                    }, status=HTTP_400_BAD_REQUEST)


@post(r'transition/approve/')
def approve_transition(request) -> Response:
    """
    Endpoint for approving transitions for workflow objects.

    Args:
    request: The incoming HTTP request.

    Returns:
    HTTP response indicating success.
    """
    content_type_name, object_id, destination_state, state_field_name = RequestDataExtractor.extract(request)
    model_class = ModelFetcher.fetch_model_class(content_type_name)
    workflow_object = ModelFetcher.fetch_workflow_object(model_class, object_id)

    valid_state_fields = StateFieldUtil.list_state_fields(model_class)
    if state_field_name and state_field_name in valid_state_fields:
        state_field_names = [state_field_name]
    else:
        state_field_names = valid_state_fields

    TransitionApprover.approve_all(request.user, workflow_object, state_field_names, destination_state)
    return Response("Transitions approved successfully.")


class StateSerializer(serializers.ModelSerializer):
    transition_meta_name = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = '__all__'

    def get_transition_meta_name(self, obj):
        """
        Retrieves the transition metadata name for a given state object.

        Args:
        obj: The state object being serialized.

        Returns:
        The name of the transition metadata.
        """
        workflow = Workflow.objects.get(
            content_type=ContentType.objects.get_for_model(self.context['workflow_object'].__class__),
            field_name=self.context['status_field_name']
        )
        source_state = getattr(self.context['workflow_object'], self.context['status_field_name'])
        transition_meta = TransitionMeta.objects.filter(workflow=workflow, source_state=source_state, destination_state=obj).first()
        return transition_meta.name if transition_meta else None


@post(r'list-available-approvals/')
def list_available_approvals(request):
    """
    Lists available approvals for the specified workflow object based on its current state.

    Args:
    request: The incoming HTTP request.

    Returns:
    HTTP response with serialized state information or an error message.
    """
    content_type_name, object_id, destination_state, state_field_name = RequestDataExtractor.extract(request)
    model_class = ModelFetcher.fetch_model_class(content_type_name)
    workflow_object = ModelFetcher.fetch_workflow_object(model_class, object_id)

    valid_state_fields = StateFieldUtil.list_state_fields(model_class)
    if state_field_name and state_field_name in valid_state_fields:
        selected_state_field_name = state_field_name
    elif valid_state_fields:
        selected_state_field_name = valid_state_fields[0]
    else:
        raise ValidationError("No valid state field found for this model.", code=HTTP_400_BAD_REQUEST)

    try:
        available_approvals = getattr(workflow_object.river, selected_state_field_name).get_available_states(
            as_user=request.user)
        serializer_context = {'workflow_object': workflow_object, 'status_field_name': selected_state_field_name}
        return Response(StateSerializer(available_approvals, many=True, context=serializer_context).data)
    except Exception as e:
        raise ValidationError(f"Error retrieving available approvals: {e}", code=HTTP_400_BAD_REQUEST)
