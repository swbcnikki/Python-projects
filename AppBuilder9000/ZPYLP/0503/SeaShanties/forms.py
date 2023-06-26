from django.forms import ModelForm
from django import forms
from .models import SeaShanties


class ShantiesForm(ModelForm):
    title = forms.CharField()
    videoURL = forms.URLField()
    lyrics = forms.TextInput(
        attrs={'size': 20, 'title': 'Shanty Lyrics'})
    artist = forms.CharField()
    year = forms.CharField()
    history = forms.TextInput(
        attrs={'size:': 10, 'title': 'Historical notes:'})

    class Meta:
        model = SeaShanties
        fields = '__all__'

