from django.urls import re_path
from django.contrib import admin
from django.urls import include

from demo.view import approve_issue, approve_shipping

urlpatterns = [
    re_path(r'^approve_issue/(?P<issue_id>\d+)/(?P<next_state_id>\d+)/$', approve_issue, name='approve_issue'),
    re_path(r'^approve_shipping/(?P<shipping_id>\d+)/(?P<next_state_id>\d+)/$', approve_shipping, name='approve_shipping'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include("river_admin.urls")),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]
