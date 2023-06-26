from django.forms import ModelForm
from django import forms
from .models import TravelDestinations


class TravelDestinationsForm(ModelForm):
    class Meta:
        model = TravelDestinations
        fields = '__all__'

