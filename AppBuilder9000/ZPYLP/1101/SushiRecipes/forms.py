from django import forms
from .models import SushiRecipes


class SushiForm(forms.ModelForm):
    class Meta:
        model = SushiRecipes
        fields = ('style', 'ingredients', 'steps', 'notes')
