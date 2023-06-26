from django.forms import ModelForm
from .models import Record, GameName


class SpeedrunForm(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'




