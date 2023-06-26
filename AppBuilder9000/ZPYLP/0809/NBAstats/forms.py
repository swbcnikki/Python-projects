from django.forms import ModelForm
from .models import Defensive_Stats, PlayerDb


class Def_Stats_Form(ModelForm):
    class Meta:
        model = Defensive_Stats
        fields = '__all__'


class PlayerDatabaseForm(ModelForm):
    class Meta:
        model = PlayerDb
        fields = '__all__'
