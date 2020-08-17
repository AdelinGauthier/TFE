from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Promo
from .forms import ContactForm


def index(request):
    if request.method == 'GET':
        promo = Promo.objects.all()
        context = {'promo': promo}
        return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            mail = ''
            msg = 'Salut Nora, je te contact via le formulaire de demande : \n'
            for item in form:
                if item.name == 'email':
                    mail = str(item.value())
                msg += str(item.value()) + '\n'
            msg += 'Merci beaucoup ! J attend ta réponse, des bisous !'
            send_mail('Formulaire de contact', str(msg), request.user,
                      ['a2l195@hotmail.fr'], fail_silently=False)
            return redirect('Accueil')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def tarifs(request):
    return render(request, 'tarifs.html')
