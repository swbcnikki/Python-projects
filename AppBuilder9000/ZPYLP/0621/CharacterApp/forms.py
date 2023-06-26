from django.forms import ModelForm
from .models import Character_create


class CharacterForm(ModelForm):
    class Meta:
        model = Character_create
        fields = '__all__'
