from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from river.models import State
from river.models.transitionmeta import TransitionMeta

from river_admin.views import get, post, delete
from river_admin.views.serializers import StateDto, CreateStateDto


@get(r'state/get/<int:pk>/')
def get_it(request, pk):
    state = get_object_or_404(State.objects.all(), pk=pk)
    return Response(StateDto(state).data, status=HTTP_200_OK)


@get(r'state/list/')
def list_it(request):
    return Response(StateDto(State.objects.all(), many=True).data, status=HTTP_200_OK)


@post(r'state/create/')
def create_it(request):
    create_state_request = CreateStateDto(data=request.data)
    if create_state_request.is_valid():
        state = create_state_request.save()
        return Response({"id": state.id}, status=HTTP_200_OK)
    else:
        return Response(create_state_request.errors, status=HTTP_400_BAD_REQUEST)


@delete(r'state/delete/<int:pk>/')
def delete_it(request, pk):
    state = get_object_or_404(State.objects.all(), pk=pk)
    state.delete()
    return Response(status=HTTP_200_OK)


@delete(r'state/delete/<int:workflow_id>/<int:pk>/')
def delete_state_from_workflow(request, workflow_id, pk):
    state = get_state(pk)
    delete_transitions_from_source(workflow_id, state)
    delete_transitions_from_destination(workflow_id, state)
    return Response(status=HTTP_200_OK)


def get_state(pk):
    """
    Get a State based on its primary key (pk)
    """
    return get_object_or_404(State.objects.all(), pk=pk)


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
