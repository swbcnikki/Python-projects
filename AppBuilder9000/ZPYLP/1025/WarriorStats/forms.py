from django import forms
from django.forms import ModelForm, widgets
from .models import *


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control input-area', 'placeholder': 'Enter Player Name'}),
            'Points_Per_Game': forms.NumberInput(attrs={'class': 'form-control input-area', 'placeholder': 'PPG'}),
            'Rebounds_Per_Game': forms.NumberInput(attrs={'class': 'form-control input-area', 'placeholder': 'RPG'}),
            'Assists_Per_Game': forms.NumberInput(attrs={'class': 'form-control input-area', 'placeholder': 'APG'}),
            'Steals_Per_Game': forms.NumberInput(attrs={'class': 'form-control input-area', 'placeholder': 'SPG'}),


        }
