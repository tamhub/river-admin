from typing import Tuple, List, Type

from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from river.models import State, TransitionMeta
from river.models.fields.state import StateField

from river_admin.views import post


def extract_request_data(request) -> Tuple[str, int, str, str]:
    """
    Extracts key data from the request needed for processing transitions.
    """
    content_type_name = request.data.get('content_type_name')
    object_id = request.data.get('object_id')
    destination_state = request.data.get('destination_state')
    state_field_name = request.data.get('state_field_name', None)
    return content_type_name, object_id, destination_state, state_field_name


def fetch_model_class_by_content_type(content_type_name: str) -> Type[Model]:
    """
    Fetches the model class associated with the specified content type name.
    """
    if not isinstance(content_type_name, str):
        raise ValueError('content_type_name must be a string')
    return get_object_or_404(ContentType.objects.all(), model=content_type_name).model_class()


def fetch_workflow_object(model_class: Type[Model], object_id: int) -> Model:
    """
    Fetches a workflow object given its model class and ID.
    """
    return get_object_or_404(model_class.objects.all(), pk=object_id)


def list_state_fields(model_class: Type[Model]) -> List[str]:
    """
    Returns a list of state field names for a given model class.
    """
    return [field.name for field in model_class._meta.get_fields() if isinstance(field, StateField)]


@post(r'transition/approve/')
def approve_transition(request) -> Response:
    """
    Approves a workflow transition based on request data.
    """
    content_type_name, object_id, destination_state, state_field_name = extract_request_data(request)
    model_class = fetch_model_class_by_content_type(content_type_name)
    workflow_object = fetch_workflow_object(model_class, object_id)

    state_field_names = [state_field_name] if state_field_name and is_valid_state_field(model_class, state_field_name) \
                        else list_state_fields(model_class)

    approve_all_transitions(request.user, workflow_object, state_field_names, destination_state)
    return Response("Transitions approved successfully.")


def is_valid_state_field(model_class: Type[Model], field_name: str) -> bool:
    """
    Checks if the given field name is a valid StateField for the specified model.
    """
    return any(isinstance(field, StateField) and field.name == field_name for field in model_class._meta.get_fields())


def approve_all_transitions(user, workflow_object: Model, state_field_names: List[str], destination_state: str = None):
    """
    Approves transitions for multiple state fields on a workflow object.
    """
    for state_field_name in state_field_names:
        approve_transition_for_field(user, workflow_object, state_field_name, destination_state)


def approve_transition_for_field(user, workflow_object: Model, state_field_name: str, destination_state: str = None):
    """
    Approves a single transition for a given state field.
    """
    river_attr = getattr(workflow_object, "river", None)
    if river_attr:
        state_field = getattr(river_attr, state_field_name, None)
        if state_field:
            destination = State.objects.get(label=destination_state) if destination_state else None
            state_field.approve(as_user=user, next_state=destination)
