from django import forms

from .models import Wrestler


class wrestlerform(forms.ModelForm):
    class Meta:
        model = Wrestler
        fields = '__all__'
