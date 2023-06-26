from django.forms import ModelForm
from .models import Drone
from django import forms


class DroneForm(ModelForm):
    class Meta:
        model = Drone
        fields = '__all__'



