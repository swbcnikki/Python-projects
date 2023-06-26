from django import forms
from django.forms import ModelForm
from .models import WebScrape, UserLogin


class WebscrapeForm(ModelForm):
    class Meta:
        model = WebScrape
        fields = ('category', 'url', 'date', 'price', 'imageUrl', 'profit')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'imageUrl': forms.TextInput(attrs={'class': 'form-control'}),
            'profit': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserLoginForm(ModelForm):
    class Meta:
        model = UserLogin
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }