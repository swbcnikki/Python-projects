from django.forms import ModelForm

from .models import HardRock


class HardRockForm(ModelForm):
    class Meta:
        model = HardRock
        fields = '__all__'
