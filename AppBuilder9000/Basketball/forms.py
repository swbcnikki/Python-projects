from django import forms
from .models import Pickup


class PickupForm(forms.ModelForm):
    class Meta:
        model = Pickup
        fields = '__all__'