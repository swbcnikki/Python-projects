from django.forms import ModelForm
from .models import Restaurants

class RestaurantForm(ModelForm):
    class Meta:
        model=Restaurants
        fields= '__all__'