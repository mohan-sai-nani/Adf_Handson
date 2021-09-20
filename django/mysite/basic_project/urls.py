"""Contains all URL mappings of basic_project"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Validate.as_view()),
]
