from django.forms import ModelForm
from .models import Moves


class MovesForm(ModelForm):
    class Meta:
        model = Moves
        fields = '__all__'