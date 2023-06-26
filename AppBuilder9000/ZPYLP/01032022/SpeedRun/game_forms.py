from django.forms import ModelForm
from .models import GameName


class GameForm(ModelForm):
    class Meta:
        model = GameName
        fields = '__all__'

