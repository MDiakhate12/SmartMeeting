from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.models import *
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.decorators import login_required


def log(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)

        user = authenticate(request, username=user.username, password=password)
        print('------------------------------------------------')
        print(user)
        print('------------------------------------------------')
        print('------------------------------------------------')
        # user = User.objects.get(email=email)

        if(user):
            login(request, user)
            return render(request, 'main/index.html')

    return render(request, 'auth/login.html')


def unlog(request):
    logout(request)
    return redirect('login')


def register(request):

    print('------------------------------------------------------------')
    print(request.META.get('HTTP_REFERRER'))
    print('------------------------------------------------------------')

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if(str(password) == str(confirm_password)):
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            login(request, user)
            return render(request, 'main/index.html')

    return render(request, 'auth/register.html')
