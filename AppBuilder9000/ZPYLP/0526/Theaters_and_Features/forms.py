from django.forms import ModelForm
from django import forms
from .models import Theaters


class TheaterForm(ModelForm):
    class Meta:
        model = Theaters
        fields = '__all__'
