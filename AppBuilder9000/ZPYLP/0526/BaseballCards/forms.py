from django import forms
from django.forms import ModelForm
from .models import BaseballCard

class BaseballCardForm(ModelForm):
    class Meta:
        model = BaseballCard
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'bats_throws': forms.Select(attrs={'class': 'form-control'}),
            'career_ba_or_era': forms.TextInput(attrs={'class': 'form-control'}),
            'career_hr_or_so': forms.TextInput(attrs={'class': 'form-control'}),
        }
