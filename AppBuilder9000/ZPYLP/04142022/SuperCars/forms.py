from django.forms import ModelForm
from .models import SuperCars

class SuperCarsForm(ModelForm):
    class Meta:
        model = SuperCars
        fields = '__all__'
