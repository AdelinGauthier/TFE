from django.shortcuts import render
from .models import Promo


def index(request):
    promo = Promo
    context = {'promo': promo}
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
