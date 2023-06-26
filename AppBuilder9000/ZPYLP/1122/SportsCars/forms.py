from django.forms import ModelForm
from .models import SportsCar


class SportsCarForm(ModelForm):
    class Meta:
        model = SportsCar
        fields = '__all__'
