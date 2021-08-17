from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models
from .forms import SignUpForm
from soins.forms import SoinsSelectForm
from .forms import EditProfileForm, Dispos

from django.urls import reverse

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import render

from django.core.mail import send_mail

from .models import SoinsList, Historique, Dispo as DispoModel


class UserView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user


def MerciRes(request):
    return render(request, 'merciReserv.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('users:profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('users:profile'))
        else:
            return redirect(reverse('users:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)


def deletePage(request):
    return render(request, 'suppressionCompte.html')


def deleteConfirmation(request):
    return render(request, 'ConfirmationSuppression.html')


def delete_user(request):
    request.user.delete()
    return render(request, 'confirmationSuppression.html')


def CreateSoinsSelect(request):
    if request.method == 'POST':
        form = SoinsSelectForm(request.POST)
        form2=request.POST.get('my_dates', None)
        if form.is_valid():
            form.save()

            msg = 'Salut Nora, serait-il possible de réserver les soins suivants : \n'
            soins = ''
            test = ''
            jour = ''
            for item in form:
                test += str(item.value())
                jour = form2
                if item.value() and item.label != 'Commentaire':
                    soins += '- ' + item.label + ', \n'
                if item.label == 'Commentaire':
                    if item.value():
                        soins += '\nCommentaire : \n' + item.value() + '\n'
            msg += str(soins) + ' \nEn date du ' + str(jour) + '\n' + '\n' + '\n'

            msg += request.user.forename + '\n'
            msg += request.user.name + '\n'
            msg += request.user.phone + '\n'
            msg += request.user.adress1 + ' ' + request.user.adress2 + '\n' + '\n'
            msg += 'Merci pour votre confiance !'
            send_mail('Réservation de soins', msg, request.user.email,
                      ['nora.mazy.contact@gmail.com'], fail_silently=False)

            usermsg = 'Bonjour,' + '\n' + '\n' + 'Merci pour votre réservation.' + '\n' + '\n'
            usermsg += str(soins) + ' \nEn date du ' + str(jour) + '\n' + '\n' + '\n'
            usermsg += 'Merci beaucoup !' + '\n' + '\n'
            usermsg += 'Nora Mazy'
            send_mail('Merci pour votre réservation', usermsg, 'nora.mazy.contact@gmail.com',
                      [request.user.email], fail_silently=False)

            return redirect('users:merci')
    else:
        form = SoinsSelectForm()
        form2 = DispoModel.objects.all().order_by('Date')
        print(form2)
    return render(request, 'profileRes.html', {'form': form, 'form2': form2})


class MesReserv(ListView):
    model = SoinsList
    template_name = 'users/soinslist_list.html'
    context_object_name = 'soin_list'

    def get_queryset(self):
        return SoinsList.objects.filter(soin=self.request.user)


class Histo(ListView):
    model = Historique
    template_name = 'users/historique_list.html'
    context_object_name = 'histo_list'

    def get_queryset(self):
        return Historique.objects.filter(historique=self.request.user)
