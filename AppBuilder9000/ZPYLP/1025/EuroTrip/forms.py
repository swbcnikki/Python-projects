from django.forms import ModelForm
from .models import Location

# shortcut template
# ModelForm queries everything from dB all at once


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
