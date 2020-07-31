from django.conf.urls import url
from . import views  # import views so we can use them in urls.
from .views import *

urlpatterns = [
    url(r'^$', views.index),
    url('Connexion/', Connexion, name="Connexion"),
    url('Register/', Registration, name="Register"),
]
