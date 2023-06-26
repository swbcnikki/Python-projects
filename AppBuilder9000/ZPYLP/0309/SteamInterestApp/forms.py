from django.forms import ModelForm
from .models import SteamInterestAppBase


class SteamInterestAppForm(ModelForm):
    class Meta:
        model = SteamInterestAppBase
        fields = '__all__'
