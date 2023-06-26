from django.forms import ModelForm
from django.forms import CheckboxInput
from .models import Sharks


class SharksForm(ModelForm):
    class Meta:
        model = Sharks
        fields = '__all__'


