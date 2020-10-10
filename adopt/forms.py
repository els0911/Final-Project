from django.forms import ModelForm

from .models import AdoptRequest


class AdoptRequestForm(ModelForm):
    class Meta:
        model = AdoptRequest
        fields = [
            'pet',
            'adopter',
        ]
