from django.forms import ModelForm
from .models import Movestate, VehicleType

class movestateForm(ModelForm):
    class Meta:
        model = Movestate
        fields = '__all__'

class vehicletypeForm(ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'