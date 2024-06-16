from django.shortcuts import render, redirect
from .models import product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    products = product.objects.all()
    return render(request, 'home.html', {'products': products })

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login Successful!"))
            return redirect('home')
        else:
            login(request, user)
            messages.success(request, ("Error logging in"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out"))
    return redirect('home')

