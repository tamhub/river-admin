from django.db.models import ProtectedError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from river.models.state import State
from river.models.workflow import Workflow
from river.models.transitionapproval import TransitionApproval
from river.models.transitionmeta import TransitionMeta
from river_admin.views import get, post, delete
from river_admin.views.serializers import StateDto, CreateStateDto


@get(r'state/get/<int:pk>/')
def get_state(request, pk):
    state = get_object_or_404(State.objects.all(), pk=pk)
    return Response(StateDto(state).data, status=HTTP_200_OK)


@get(r'state/list/')
def list_states(request):
    slug = request.GET.get('slug').lower() if request.GET.get('slug') else None
    if slug:
        states = State.objects.filter(slug__contains=slug)
    else:
        states = State.objects.all()
    return Response(StateDto(states, many=True).data, status=HTTP_200_OK)


@post(r'state/create/')
def create_state(request):
    create_state_request = CreateStateDto(data=request.data)
    if create_state_request.is_valid():
        state = create_state_request.save()
        return Response({"id": state.id}, status=HTTP_200_OK)
    else:
        return Response(create_state_request.errors, status=HTTP_400_BAD_REQUEST)


@delete(r'state/delete/<int:pk>/')
def delete_state(request, pk):
    state = get_object_or_404(State.objects.all(), pk=pk)
    try:
        state.delete()
    except ProtectedError as e:
        return Response({"message": str(e)}, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_200_OK)


@delete(r'state/delete/<int:workflow_id>/<int:pk>/')
def delete_state_from_workflow(request, workflow_id, pk):
    state = get_state_by_pk(pk)
    workflow = get_workflow_by_pk(workflow_id)
    update_instances_with_previous_state(workflow, state)
    reset_initial_state_for_instances(workflow, state)
    delete_state_transitions(workflow_id, state)
    return Response(status=HTTP_200_OK)


# Helper functions

def get_state_by_pk(pk):
    """
    Get a State based on its primary key (pk)
    """
    return get_object_or_404(State.objects.all(), pk=pk)


def get_workflow_by_pk(workflow_id):
    """
    Get a Workflow based on its primary key (workflow_id)
    """
    return get_object_or_404(Workflow, pk=workflow_id)


def update_instances_with_previous_state(workflow, state):
    """
    Update instances related to the workflow, setting their state to the previous state
    """
    model_class = workflow.content_type.model_class()
    for instance in model_class.objects.filter(**{workflow.field_name: state}):
        previous_transition = TransitionApproval.objects.filter(
            workflow=workflow,
            transition__destination_state=state,
            object_id=instance.pk,
            content_type=workflow.content_type
        ).order_by('-transaction_date').first()

        if previous_transition:
            previous_state = previous_transition.transition.source_state
            setattr(instance, workflow.field_name, previous_state)
            instance.save()


def reset_initial_state_for_instances(workflow, state):
    """
    Reset the state of instances related to the workflow to the initial state
    """
    model_class = workflow.content_type.model_class()
    model_class.objects.filter(**{workflow.field_name: state}).update(**{workflow.field_name: workflow.initial_state})


def delete_state_transitions(workflow_id, state):
    """
    Delete TransitionMeta instances related to the state and workflow
    """
    delete_transitions_from_source(workflow_id, state)
    delete_transitions_from_destination(workflow_id, state)


def delete_transitions_from_source(workflow_id, state):
    """
    Delete TransitionMeta instances where the State is the "source state"
    """
    TransitionMeta.objects.filter(workflow_id=workflow_id, source_state=state).delete()


def delete_transitions_from_destination(workflow_id, state):
    """
    Delete TransitionMeta instances where the State is the "destination state"
    """
    TransitionMeta.objects.filter(workflow_id=workflow_id, destination_state=state).delete()
