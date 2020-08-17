import os

from django.db import models

from noraMazy import settings


class Promo(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="namePromo")
    photoPromo = models.ImageField(upload_to='promo/', blank=True, null=True, verbose_name="photoPromo")

    def __unicode__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.photoPromo.name)


class ContactFo(models.Model):
    name = models.CharField(blank=True, max_length=254)
    email = models.CharField(blank=True, max_length=254)
    msg = models.TextField(null=True, blank=True)
