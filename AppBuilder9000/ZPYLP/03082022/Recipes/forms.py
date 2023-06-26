from django.forms import ModelForm
from .models import Recipes


class RecipesForm(ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
