from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def login(request):
    return render(request, 'Registration/login.html')

def Registration(request):
    return render(request, 'Registration.html')
