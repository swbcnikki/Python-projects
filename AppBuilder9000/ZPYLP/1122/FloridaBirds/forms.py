
from django import forms
from django.forms import ModelForm
from .models import BirdDescription


# ModelForm parameter directly converts a model in to django form.


class BirdDescriptionForm(ModelForm):
    # class Meta used to customize model fields like changing the order of fields etc.
    class Meta:
        model = BirdDescription  # tells which model to create form from.
        fields = '__all__'  # indicates all fields in the model should be used.

        widgets = {
            'bird_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_seen': forms.TextInput(attrs={'class': 'form-control','placeholder':'mm/dd/yyyy'}),
            'habitat': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),

        }
