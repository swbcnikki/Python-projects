from django.forms import ModelForm
from .models import Games


class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = '__all__'
