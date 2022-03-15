from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogView, name='blogView'),
    path('addBlog/', views.addBlog, name='addBlog'),
    path('<int:pk>/', views.detailBlog, name='detailBlog'),
]
