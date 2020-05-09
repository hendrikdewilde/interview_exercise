# from django.contrib import admin
from django.urls import path, include, re_path

from cases import views

urlpatterns = [
    re_path(r'^$', views.cases_index,
            name='cases_index_page'),

]
