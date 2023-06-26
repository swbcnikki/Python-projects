from django.forms import ModelForm
from .models import FunkoPopName
from django import forms

# collecting the information from the .model to to be able to input into the database information for each input from
# the web page form and save the imputed information into the database.


class CollectionForm(ModelForm):

    class Meta:
        model = FunkoPopName
        fields = '__all__'
        #
        labels = {
            'size': 'Size',
            'name': '',
            'fandome': '',
            'chase': 'Chase(rare)',
            'purchase_price': '',
            'value': '',
        }
        # Bootstrap styling for input form for addcollection.html
        widgets = {
            'size': forms.Select(attrs={'class': 'btn btn-light dropdown-toggle'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'fandome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fandom'}),
            'chase': forms.Select(attrs={'class': 'btn btn-light dropdown-toggle'}),
            'purchase_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purchase Price'}),
            'value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Value'}),
        }
