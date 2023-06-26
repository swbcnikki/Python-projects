from django import forms
from django.forms import ModelForm
from .models import Motorcycle, Route

# Create a motorcycle form
class MotorcycleForm(ModelForm):
    class Meta:
        model = Motorcycle
        fields = '__all__'
# Could do all or a tuple of certain values

        widgets = {
            'ENGINE_SIZE': forms.TextInput(attrs={'class': 'form-control'}),
            'MODEL_TYPE': forms.TextInput(attrs={'class': 'form-control'}),
            }
# Create a route form
class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'START_DESTINATION': forms.TextInput(attrs={'class': 'form-control'}),
            'END_DESTINATION': forms.TextInput(attrs={'class': 'form-control'}),
        }