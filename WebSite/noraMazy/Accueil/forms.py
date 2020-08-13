from .models import ContactFo
from django.forms import ModelForm


class ContactForm(ModelForm):
    template_name = '/contact/'

    class Meta:
        model = ContactFo
        fields = '__all__'
        labels = {
            'name': 'Nom',
            'email': 'Email',
            'msg': 'Votre message',
        }
