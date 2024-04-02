from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from river_admin.views import post


# Helper function to extract data from request
def extract_data(request):
    content_type_name = request.data.get('content_type_name')
    object_id = request.data.get('object_id')
    destination_state = request.data.get('destination_state')
    return content_type_name, object_id, destination_state


# Helper function for getting model class
def get_model_class(content_type_name):
    return ContentType.objects.get(model=content_type_name).model_class()


# helper function to get workflow object
def get_workflow_object(model_class, object_id):
    return get_object_or_404(model_class.objects.all(), pk=object_id)


# Helper function for getting status field name
def get_status_field_name(workflow_object):
    return getattr(workflow_object, workflow_object.workflow.status_field)


@post(r'transition/approve/')
def approve_transition(request):
    content_type_name, object_id, destination_state = extract_data(request)
    model_class = get_model_class(content_type_name)
    workflow_object = get_workflow_object(model_class, object_id)
    status_field_name = get_status_field_name(workflow_object)
    user = request.user
    try:
        getattr(workflow_object.river, status_field_name).approve(as_user=user)
    except Exception as e:
        return Response(str(e), status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_200_OK)
