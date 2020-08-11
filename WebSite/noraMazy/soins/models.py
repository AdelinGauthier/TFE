from django.db import models
import datetime
from django.conf import settings
from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class SoinsSelect(models.Model):
    extensionsCils = models.BooleanField(default=False)
    lashLift = models.BooleanField(default=False)
    lashLiftTeinture = models.BooleanField(default=False)
    browLift = models.BooleanField(default=False)
    browliftTeinture = models.BooleanField(default=False)
    browlifthenne = models.BooleanField(default=False)
    browLift3dFiller = models.BooleanField(default=False)
    browlif3dTeinture = models.BooleanField(default=False)
    browlif3dhenne = models.BooleanField(default=False)
    hennaBrow = models.BooleanField(default=False)
    soin3d = models.BooleanField(default=False)
    teintureCils = models.BooleanField(default=False)
    teintureSourcils = models.BooleanField(default=False)
    epilationSourcil = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today)


class FichesClients(models.Model):
    Client = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Soins = models.TextField(default='')
    Description = models.TextField(default='')
    Histoire = models.TextField(default='')
    Historique = models.TextField(default='')
    Fidelite = models.IntegerField(default=0)
    Date = models.DateField(default=datetime.date.today)



