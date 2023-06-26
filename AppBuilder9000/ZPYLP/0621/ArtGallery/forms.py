
from django.forms import ModelForm
from .models import Artist
from django import forms

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
