from django.forms import ModelForm
from django import forms
from .models import Activity, WeatherMoment


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_name', 'activity_snacks', 'activity_description', 'distance']


class WeatherMomentForm(ModelForm):
    class Meta:
        model = WeatherMoment
        fields = "__all__"
