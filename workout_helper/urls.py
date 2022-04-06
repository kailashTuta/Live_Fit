from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workouts, name='workouts'),
    path('<int:pk>/', views.workoutDetails, name='workoutDetails'),
]
