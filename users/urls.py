from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView, signup, CreateSoinsSelect, MesReserv, Histo, MerciRes
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/',  login_required(UserView.as_view(template_name='profile.html')), name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('signup/', signup, name='signup'),
    path('profile/reservation', CreateSoinsSelect, name="reservation"),
    path('profile/Mes_reservation', MesReserv.as_view(), name="mesReserv"),
    path('profile/Mon_historique', Histo.as_view(), name="monHisto"),
    path('profile/merci', MerciRes.as_view(), name="merci"),

]