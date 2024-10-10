from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from river_admin.views import get, post, put, delete
from river.models.feature_panel import FeatureSetting
from river_admin.views.serializers import FeatureSettingDto


@get(r'feature_setting/get/<str:feature>/')
def get_it(request, feature):
    feature_setting = get_object_or_404(FeatureSetting.objects.all(), feature=feature)
    return Response(FeatureSettingDto(feature_setting).data, status=HTTP_200_OK)


@get(r'feature_setting/list/')
def list_it(request):
    return Response(FeatureSettingDto(FeatureSetting.objects.all(), many=True).data, status=HTTP_200_OK)


@put(r'feature_setting/update/<str:feature>/')
def update_it(request, feature):
    try:
        feature_setting = FeatureSetting.objects.get(feature=feature)
        serializer = FeatureSettingDto(feature_setting, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    except FeatureSetting.DoesNotExist:
        serializer = FeatureSettingDto(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(feature=feature)

    return Response(serializer.data, status=HTTP_200_OK)
