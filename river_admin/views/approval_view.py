from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from river.models.fields.state import StateField

from river_admin.views import post


def retrieve_requested_data(request):
    """
    Retrieve Requested Data

    This method retrieves specific data from the provided request object.

    Parameters:
        request (object): The request object containing the desired data.

    Returns:
        tuple: A tuple containing the values of 'content_type_name', 'object_id', and 'destination_state' extracted from the request data.

    """
    return request.data.get('content_type_name'), request.data.get('object_id'), request.data.get('destination_state')


def get_linked_model_class(content_type_name):
    """
    Retrieves the model class associated with the given content type name.

    Args:
        content_type_name (str): The name of the content type.

    Returns:
        model_class (class): The model class associated with the content type.

    Raises:
        ContentType.DoesNotExist: If the content type does not exist in the database.

    """
    if not isinstance(content_type_name, str):
        raise ValueError('content_type_name must be a string')

    return get_object_or_404(ContentType.objects.all(), model=content_type_name).model_class()


def get_related_workflow_object(model_class, object_id):
    """
    Get the related workflow object for a given model and object ID.

    :param model_class: The model class from which to get the related workflow object.
    :type model_class: django.db.models.Model
    :param object_id: The ID of the object for which to get the related workflow object.
    :type object_id: int
    :return: The related workflow object.
    :rtype: django.db.models.Model
    :raises django.http.Http404: If the related workflow object does not exist.
    """
    return get_object_or_404(model_class.objects.all(), pk=object_id)


def get_related_state_field_names(model_class):
    """
    Get the names of related state fields for a given model class.

    :param model_class: The model class for which to retrieve the related state field names.
    :type model_class: type
    :return: A list of names of related state fields for the given model class.
    :rtype: list[str]
    """
    return [field.name for field in model_class._meta.get_fields() if isinstance(field, StateField)]


@post(r'transition/approve/')
def approve_transition(request):
    """
    Approve Transition

    Processes the approval of a transition in a workflow.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The HTTP response indicating the status of the processing.
    """
    content_type_name, object_id, destination_state = retrieve_requested_data(request)
    model_class = get_linked_model_class(content_type_name)
    workflow_object = get_related_workflow_object(model_class, object_id)
    status_field_names = get_related_state_field_names(model_class)
    try:
        approve_transitions(request.user, workflow_object, status_field_names)
        return Response("Transitions approved successfully.")
    except Exception as e:
        raise ValidationError(f"Error approving transitions: {e}", code=HTTP_400_BAD_REQUEST)


def approve_transitions(user, workflow_object, status_field_names):
    """
    Approves transitions for multiple status fields.

    Parameters:
    - user (str): The user who is approving the transitions.
    - workflow_object (object): The object on which the transitions will be approved.
    - status_field_names (list[str]): A list of status field names for which the transitions will be approved.

    Returns:
    None

    Example Usage:
    user = "John"
    workflow_object = WorkflowObject()
    status_fields = ["Status1", "Status2"]
    approve_transitions(user, workflow_object, status_fields)
    """
    for status_field_name in status_field_names:
        approve_single_transition(user, workflow_object, status_field_name)


def approve_single_transition(user, workflow_object, status_field_name):
    """
    Approves a single transition in the workflow for the specified user.

    Parameters:
    - user (object): The user who is approving the transition.
    - workflow_object (object): The object containing the workflow.
    - status_field_name (str): The name of the status field associated with the transition.

    Returns: None

    Example usage:
    approve_single_transition(user, workflow_object, "status")

    Note:
    This method assumes that the workflow object has a property called "river" and that the status field identified by status_field_name exists and is callable.
    """
    river_attr = getattr(workflow_object, "river", None)
    if river_attr and hasattr(river_attr, status_field_name):
        status_field_attr = getattr(river_attr, status_field_name)
        status_field_attr.approve(as_user=user)


@post(r'list-available-approvals/')
def list_available_approvals(request):
    """
    List Available Approvals

    Lists the available approvals for a user.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The HTTP response containing the list of available approvals.
    """
    content_type_name, object_id, _ = retrieve_requested_data(request)
    model_class = get_linked_model_class(content_type_name)
    workflow_object = get_related_workflow_object(model_class, object_id)
    status_field_name = get_related_state_field_names(model_class)[0]
    try:
        available_approvals = getattr(workflow_object.river, status_field_name).get_available_states(as_user=request.user)
        data = {
            "available_approvals": available_approvals
        }
        return Response(data)
    except Exception as e:
        raise ValidationError(f"Error retrieving available approvals: {e}", code=HTTP_400_BAD_REQUEST)