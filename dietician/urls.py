from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dietician', views.dietician, name='dietician'),
    path('reports', views.dietReport, name='reports'),
]
