from django.forms import ModelForm
from .models import Music


class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = '__all__'

