from django.forms import ModelForm
from django import forms
from .models import MyCarParts



class MyCarPartsForm(ModelForm):
    class Meta:
        model = MyCarParts
        fields = '__all__'

