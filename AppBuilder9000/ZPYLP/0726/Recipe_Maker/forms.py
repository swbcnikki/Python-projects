from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_type', 'recipe_name', 'recipe_ingredients', 'recipe_instructions')

        widgets = {
            'recipe_type': forms.Select(attrs={'class': 'btn btn-light dropdown-toggle'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'recipe_instructions': forms.Textarea(attrs={'class': 'form-control'}),
        }


"""
 old code to experiment with later

# instead of grabbing a class from model.py, its grabbing from admin.py
# class RecipeAdmin has models Ingredients and Instructions inline
from .admin import RecipeAdmin


class RecipeForm(ModelForm):
    class Meta:
        model = RecipeAdmin
        # instead of writing out all the fields from the model, use '__all__'
        # grabs all the fields from within RecipeAdmin
        # passes it into the form
        fields = '__all__'
"""
