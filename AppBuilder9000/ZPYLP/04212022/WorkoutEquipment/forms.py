from django.forms import ModelForm
from .models import WorkoutEquipment


class WorkoutEquipmentForm(ModelForm):
    class Meta:
        model = WorkoutEquipment
        fields = '__all__'

