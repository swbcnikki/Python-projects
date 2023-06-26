from django.forms import ModelForm
from django import forms
from .models import Cbooks


class ComicForm(ModelForm):
    class Meta:
        model = Cbooks
        fields = '__all__'
