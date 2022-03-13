from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.


def blogView(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})
