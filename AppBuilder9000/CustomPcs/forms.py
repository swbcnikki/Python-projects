# Importing the models from the models.py
from django import forms
from .models import Builds


# Creating the form for the model
class BuildForm(forms.ModelForm):
    class Meta:
        model = Builds
        fields = "__all__"

