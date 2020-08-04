from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'forename', 'adress1', 'adress2', 'dateNaiss')


