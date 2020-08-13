from django.forms import ModelForm
from .models import SoinsSelect
from django.db import models as db_models
from django import forms


class SoinsSelectForm(ModelForm):
    class Meta:
        model = SoinsSelect
        fields = '__all__'
        labels = {
            'extensionsCils': 'Lash Extensions - One by One',
            'lashLift': 'Lashlift',
            'lashLiftTeinture': 'Lashlift + Teinture',
            'browLift': 'Browlift',
            'browLift3dFiller': 'Browlift + 3D Filler',
            'browliftTeinture': 'Browlift + Teinture',
            'browlifthenne': 'Browlift + Henna Brows',
            'browlif3dTeinture': 'Browlift + 3D Filler + Teinture',
            'browlif3dhenne': 'Browlift + 3D Filler + Henna Brows',
            'hennaBrow': 'Henna Brows',
            'teintureCils': 'Teinture Cils',
            'teintureSourcils': 'Teinture Sourcils',
            'epilationSourcil': 'Epilation Sourcils',
            'soin3d': 'Cure 3D Filler',
            'date': 'Date',
        }


class SoinsSelectForm1(ModelForm):
    date = db_models.DateField()

