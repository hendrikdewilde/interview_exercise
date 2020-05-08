# from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from api import views
from api.views_auth_token import obtain_auth_token_custom

router = routers.DefaultRouter()
# router.register(r'networks', views.NetworksViewSet, basename='Network')
# router.register(r'connection', views.ConnectionViewSet, basename='Connection')


urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Standard
    path('api-token-auth/', obtain_auth_token_custom, name='api_token_auth'),
]
