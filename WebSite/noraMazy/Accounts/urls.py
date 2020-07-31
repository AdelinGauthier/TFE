from django.contrib.auth.views import LoginView
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'Registration', views.Registration),
]
