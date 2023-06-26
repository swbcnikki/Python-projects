from django.forms import ModelForm
from .models import Child, Coach


class coachForm(ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'

class childForm(ModelForm):
    class Meta:
        model = Child
        fields = '__all__'