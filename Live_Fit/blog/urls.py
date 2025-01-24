from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogView, name='blogView'),
    path('addBlog/', views.addBlog, name='addBlog'),
    path('editBlog/<int:pk>', views.editBlog, name='editBlog'),
    path('dashboardBlog', views.dashboardBlog, name='dashboardBlog'),
    path('<int:pk>/', views.detailBlog, name='detailBlog'),
    path('deleteBlog/<int:pk>', views.deleteBlog, name='deleteBlog'),
]
