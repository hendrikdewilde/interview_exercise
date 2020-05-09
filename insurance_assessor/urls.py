# from django.contrib import admin
from django.urls import path, include, re_path

from insurance_assessor import views

urlpatterns = [
    re_path(r'^$', views.insurance_assessor_index,
            name='insurance_assessor_index_page'),

]
