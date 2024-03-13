from django.urls import re_path
from rest_framework.authtoken.views import obtain_auth_token

from river_admin.views import urls

urlpatterns = [
                  re_path(r'^api-token-auth/', obtain_auth_token),
              ] + urls
