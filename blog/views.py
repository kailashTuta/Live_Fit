from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Post
from .forms import AddBlog

# Create your views here.


def blogView(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def addBlog(request):
    form = AddBlog(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            image = form.cleaned_data['image']
            instance = form.save(commit=False)
            instance.author = request.user
            instance.slug = slugify(instance.title)
            instance.save()
            return redirect('/blog')
        else:
            form = AddBlog()
    context = {'form': form}
    return render(request, 'blog/addBlog.html', context)
