from django.forms import ModelForm
from django import forms
from .models import Entry, WeatherMoment


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'body']


class WeatherMomentForm(ModelForm):
    class Meta:
        model = WeatherMoment
        fields = "__all__"
