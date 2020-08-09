from django.conf.urls import url
from django.conf.urls.static import static

from noraMazy import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='Accueil'),
    url('contact', views.contact, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
