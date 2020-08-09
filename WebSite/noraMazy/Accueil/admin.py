from django.contrib import admin
from .models import Promo

class AccueilPromo(admin.ModelAdmin):
    list = 'photoPromo'


admin.site.register(Promo, AccueilPromo)
