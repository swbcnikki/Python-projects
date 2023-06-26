from django import forms
from django.forms import ModelForm, widgets
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control input-area', 'placeholder': 'Item Name'}),
            'ItemType': forms.TextInput(attrs={'class': 'form-control input-area', 'placeholder': 'Item Type'}),
            'ItemAmount': forms.NumberInput(attrs={'class': 'form-control input-area', 'placeholder': 'Amount'}),



        }
