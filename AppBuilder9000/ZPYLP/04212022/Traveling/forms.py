from .models import Place, Traveler
from django.forms import ModelForm

class TravelerForm(ModelForm):
    class Meta:
        model = Traveler
        fields = '__all__'

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'