from django.forms import ModelForm
from .models import TheForce
from django import forms

class TheForceForm(forms.ModelForm):
    class Meta:
        model = TheForce
        fields = '__all__'
