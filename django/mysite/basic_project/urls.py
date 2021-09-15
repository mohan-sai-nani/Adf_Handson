"""Contains all URL mappings of basic_project"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('validate', views.validate, name='validate'),
]
