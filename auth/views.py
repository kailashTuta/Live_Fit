from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
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
        myuser.is_active = False
        myuser.save()
        messages.success(
            request, 'User created successfully and Please Confirm your email')

        # Welcome Email
        subject = "Welcome to Live Fit"
        message = "Hello " + myuser.first_name + "!! \n" + \
            "Welcome to Live Fit \n Thanks for signing up \n we have also sent you a confirmation email, please confirm your email adddress to complete your activation of account. \n\n Thanking You\n Live Fit Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confimrmation mail
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ LiveFit"
        message2 = render_to_string('mail/email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': force_str(urlsafe_base64_encode(force_bytes(myuser.pk))),
            'token': generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email])
        email.fail_silently = True
        email.send()

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


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        auth_login(request, myuser)
        messages.success(request, 'Account activated successfully')
        return redirect('home')
    else:
        messages.error(request, 'Invalid activation link')
        return render(request, 'mail/activation_failed.html')
