from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Account
from blog.models import Post
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Live_Fit import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token

# Create your views here.

def home(request):
    return render(request, 'auth/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        if len(username) > 20:
            messages.error(request, 'Username must be less than 20 characters')
            return redirect('register')

        if password != cpassword:
            messages.error(request, 'Password does not match')
            return redirect('register')

        myuser = User.objects.create_user(
            username=username, email=email, password=password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        user = User.objects.get(username=username)
        account = Account(user=user)
        account.save()
        messages.success(request, 'User created successfully')

        return redirect('login')
    return render(request, 'auth/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            name = user.username
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'auth/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    posts = Post.objects.filter(author=request.user).order_by('-pk')[:2]
    context = {
        'user': request.user,
        'posts': posts
    }
    return render(request, 'auth/dashboard.html', context)