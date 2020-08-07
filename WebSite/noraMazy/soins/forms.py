from django.forms import ModelForm
from .models import SoinsSelect
from django.db import models as db_models


class SoinsSelectBox(ModelForm):
    class Meta:
        model = SoinsSelect
        fields = '__all__'


class SoinsSelectForm(ModelForm):
    date = db_models.DateField()
    fields = SoinsSelectBox.Meta.fields + 'date'
