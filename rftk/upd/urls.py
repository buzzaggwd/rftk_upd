from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("create-section-ajax/", views.create_section_ajax, name="create_section_ajax"),
]