from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import AddBlog

# Create your views here.


@login_required(login_url='login')
def blogView(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


@login_required(login_url='login')
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


@login_required(login_url='login')
def editBlog(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        form = AddBlog(request.POST or None,
                       request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.slug = slugify(instance.title)
            instance.save()
            return HttpResponseRedirect('/blog/dashboardBlog')
    else:
        post = Post.objects.get(pk=pk)
        form = AddBlog(instance=post)
    return render(request, 'blog/editBlog.html', {'form': form})


def deleteBlog(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        print(post)
        post.delete()
        return HttpResponseRedirect('/blog/dashboardBlog')


@login_required(login_url='login')
def detailBlog(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'blog/blogDetails.html', context)


@login_required(login_url='login')
def dashboardBlog(request):
    context = {
        'user': request.user,
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'blog/blogDashboard.html', context)
