from django.forms import ModelForm
from .models import Players
from .models import Stats

class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class StatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = '__all__'