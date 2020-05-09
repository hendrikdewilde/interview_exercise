# from django.contrib import admin
from django.urls import path, include, re_path

from insurance_companies import views

urlpatterns = [
    re_path(r'^$', views.insurance_companies_index,
            name='insurance_companies_index_page'),

]
