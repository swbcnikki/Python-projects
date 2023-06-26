from django.forms import ModelForm
from .models import Player, Team


# shortcut template
# queries everything from dB all at once, ModelForm does that
class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
