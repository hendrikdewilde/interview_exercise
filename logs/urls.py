# from django.contrib import admin
from django.urls import path, include, re_path

from logs import views

urlpatterns = [
    re_path(r'^$', views.logs_index, name='logs_index_page'),

]
