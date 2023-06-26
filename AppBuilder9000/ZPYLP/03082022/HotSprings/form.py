from django.forms import ModelForm
from .models import HotSprings, Location

class hotspringsForm(ModelForm):
    class Meta:
        model = HotSprings
        model = Location
        fields = '__all__'
