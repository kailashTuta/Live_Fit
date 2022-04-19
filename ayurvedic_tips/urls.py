from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ayurvedicTips, name='ayurvedicTips'),
    path('<int:pk>/', views.tipDetails, name='tipDetails'),
]
