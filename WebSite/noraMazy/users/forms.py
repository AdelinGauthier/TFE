from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'forename', 'adress1', 'adress2', 'dateNaiss', 'phone')
        labels = {
            'email': 'Adresse mail',
            'name': 'Nom',
            'forename': 'Prénom',
            'adress1': 'Adresse 1',
            'adress2': 'Adresse 2',
            'dateNaiss': 'Date de naissance',
            'phone': 'N° téléphone',
        }


class EditProfileForm(UserChangeForm):
    template_name = '/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'forename',
            'password',
            'adress1',
            'adress2',
            'phone'
        )
        labels = {
            'email': 'Adresse mail',
            'name': 'Nom',
            'forename': 'Prénom',
            'password': 'Mot de passe',
            'adress1': 'Adresse 1',
            'adress2': 'Adresse 2',
            'phone': 'N° téléphone',
        }


