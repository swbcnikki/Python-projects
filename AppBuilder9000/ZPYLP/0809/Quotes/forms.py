from django.forms import ModelForm, TextInput
from .models import Quote
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .Subject import SUBJECT


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'Author': forms.TextInput(attrs={'class': 'form-control'}),
            'Quote': forms.TextInput(attrs={'class': 'form-control'}),
            'Year': forms.TextInput(attrs={'class': 'form-control'}),
        }
