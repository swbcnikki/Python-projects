from django.forms import ModelForm, TextInput
from django.forms.widgets import DateInput
from .models import City, Facts
from django import forms


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}


class FactForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = "__all__"
        widgets = {
            'date': DateInput(attrs={'type': 'date'})}







