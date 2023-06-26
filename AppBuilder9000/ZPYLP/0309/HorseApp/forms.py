from django.forms import ModelForm
from .models import RaceHorse

# form model for racehorse


class RaceHorseForm(ModelForm):
    class Meta:
        model = RaceHorse
        fields = '__all__'
