from django.http import HttpResponse
from django.template import Context, loader

from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')
