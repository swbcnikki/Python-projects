# Imports;
from django.forms import ModelForm
from django import forms
from .models import Skater, WeatherMoment

# Forms;
class EntryForm(ModelForm):
    class Meta:
        model = Skater
        fields = ['first_name', 'last_name', 'age', 'hometown']

class WeatherMomentForm(ModelForm):
    class Meta:
        model = WeatherMoment
        fields = "__all__"