from django.forms import ModelForm
from .models import BoardGame


class BoardGameForm(ModelForm):
    class Meta:
        model = BoardGame
        fields = '__all__'
