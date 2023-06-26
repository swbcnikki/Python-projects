from django.forms import ModelForm
from .models import Players, Teams


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class TeamsForm(ModelForm):
    class Meta:
        model = Teams
        fields = '__all__'
