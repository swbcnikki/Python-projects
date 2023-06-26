from django.forms import ModelForm
from django import forms
from .models import Recipe




# Creating form class
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['cuisine_type', 'recipe_name', 'ingredients', 'date_created']
        widgets = {
            'cuisine_type': forms.TextInput(attrs={'class': 'cuisine_type', 'placeholder': 'Type of Cuisine'}),
            'recipe_name': forms.TextInput(attrs={'class': 'recipe_name', 'placeholder': 'Name of Recipe'}),
            'ingredients': forms.TextInput(attrs={'class': 'ingredients', 'placeholder': 'List of Ingredients'}),
            'date_created': forms.DateInput(attrs={'class': 'date_created', 'placeholder': 'Date Added:', 'type': 'date'}),
            }



