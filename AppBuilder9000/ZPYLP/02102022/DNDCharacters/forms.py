from django.forms import ModelForm
from .models import Characters
from django import forms

class CharacterForm(ModelForm):
    class Meta:
        model = Characters
        fields = '__all__'

        widgets = {
              'Character_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name your character'}),
              'Character_Class': forms.Select(attrs={'class': 'form-control'}),
              'Strength': forms.Select(attrs={'class': 'form-control'}),
              'Dexterity': forms.Select(attrs={'class': 'form-control'}),
              'Constitution': forms.Select(attrs={'class': 'form-control'}),
              'Intellegence': forms.Select(attrs={'class': 'form-control'}),
              'Wisdom': forms.Select(attrs={'class': 'form-control'}),
              'Charisma': forms.Select(attrs={'class': 'form-control'}),
              'Background': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your story'}),
       }
