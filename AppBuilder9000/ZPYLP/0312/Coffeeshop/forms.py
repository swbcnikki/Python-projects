from django.forms import ModelForm

from .models import Drink, Recipe


class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = '__all__'


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
