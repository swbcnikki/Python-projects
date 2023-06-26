from django.forms import ModelForm
from django import forms
from .models import Trails

class TrailForm(ModelForm):
    class Meta:
        model = Trails
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'difficulty': forms.RadioSelect(attrs={'class': 'form-control'}),
            'miles': forms.TextInput(attrs={'class': 'form-control'}),
            'camping': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
        }