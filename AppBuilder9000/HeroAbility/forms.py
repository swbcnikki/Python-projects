from django.forms import ModelForm
from .models import Heroes


class HeroForm(ModelForm):
    class Meta:
        model = Heroes #use the Heroes model
        fields = '__all__'
