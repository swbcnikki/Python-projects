from django.forms import ModelForm
from .models import Yoga
from django import forms

class YogaForm(forms.ModelForm):
    class Meta:
        model = Yoga
        fields = '__all__'