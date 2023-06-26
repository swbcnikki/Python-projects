from django import forms  # import form class from django
from .models import ChefKnives  # import ChefKnives from models.py


# create a ModelForm
class KnifeForm(forms.ModelForm):
    # create metaclass
    class Meta:
        # specify model to be used
        model = ChefKnives
        # specify fields to be used
        fields = '__all__'


class SearchForm(forms.Form):
    x = forms.CharField(max_length=100)
