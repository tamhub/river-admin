from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from river_admin.views import get, post, put, delete
from river.models.feature_panel import FeatureSetting
from river_admin.views.serializers import FeatureSettingDto


@get(r'feature_setting/get/<int:pk>/')
def get_it(request, pk):
    feature_setting = get_object_or_404(FeatureSetting.objects.all(), pk=pk)
    return Response(FeatureSettingDto(feature_setting).data, status=HTTP_200_OK)


@get(r'feature_setting/list/')
def list_it(request):
    return Response(FeatureSettingDto(FeatureSetting.objects.all(), many=True).data, status=HTTP_200_OK)


@post(r'feature_setting/create/')
def create_it(request):
    create_feature_setting_request = FeatureSettingDto(data=request.data)
    if create_feature_setting_request.is_valid():
        feature_setting = create_feature_setting_request.save()
        return Response({"id": feature_setting.id}, status=HTTP_200_OK)
    else:
        return Response(create_feature_setting_request.errors, status=HTTP_400_BAD_REQUEST)


@put(r'feature_setting/update/<int:pk>/')
def update_it(request, pk):
    feature_setting = get_object_or_404(FeatureSetting.objects.all(), pk=pk)
    update_feature_setting_request = FeatureSettingDto(data=request.data, instance=feature_setting)

    if update_feature_setting_request.is_valid():
        update_feature_setting_request.save()
        return Response({"message": "Feature setting is updated"}, status=HTTP_200_OK)
    else:
        return Response(update_feature_setting_request.errors, status=HTTP_400_BAD_REQUEST)


@delete(r'feature_setting/delete/<int:pk>/')
def delete_it(request, pk):
    feature_setting = get_object_or_404(FeatureSetting.objects.all(), pk=pk)
    feature_setting.delete()
    return Response(status=HTTP_200_OK)
