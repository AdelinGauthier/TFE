from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from captcha.fields import ReCaptchaField
from django.db import models as db_models

from .models import User, Dispo
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        captcha = ReCaptchaField()
        fields = ('email', 'name', 'forename', 'adress1', 'adress2', 'dateNaiss', 'phone')
        labels = {
            'email': 'Adresse mail',
            'name': 'Nom',
            'forename': 'Prénom',
            'adress1': 'Adresse (Rue + Numéro)',
            'adress2': 'Adresse (Code postal + localité)',
            'dateNaiss': 'Date de naissance',
            'phone': 'N° téléphone',
        }
        widgets = {
            'dateNaiss': DateInput(),
        }


class EditProfileForm(UserChangeForm):
    template_name = '/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'forename',
            'adress1',
            'adress2',
            'phone'
        )
        labels = {
            'email': 'Adresse mail',
            'name': 'Nom',
            'forename': 'Prénom',
            'adress1': 'Adresse 1',
            'adress2': 'Adresse 2',
            'phone': 'N° téléphone',
        }


class Dispos(ModelForm):
    class Meta:
        model = Dispo
        fields = ('Date',)
        labels = {
            'Date': 'Date',
        }