# from django.contrib import admin
from django.urls import path, include, re_path

from claims import views

urlpatterns = [
    re_path(r'^$', views.claims_index,
            name='claims_index_page'),

]
