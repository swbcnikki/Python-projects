from django .forms import ModelForm
from .models import ResortListings
from django import forms


class ResortListingsForm(ModelForm):
    class Meta:
        model = ResortListings
        fields = '__all__'