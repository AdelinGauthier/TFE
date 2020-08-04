from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'forename', 'adress1', 'adress2', 'dateNaiss')


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
            'adress2'
        )
