from django.forms import ModelForm
from .models import Airplane

class Airplaneform(ModelForm):
    class Meta:
        model = Airplane
        fields = '__all__'
