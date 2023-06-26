from django.forms import ModelForm
from .models import Recipe
from django.forms import Form, CharField

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class APIForm(Form):
    query = CharField()


