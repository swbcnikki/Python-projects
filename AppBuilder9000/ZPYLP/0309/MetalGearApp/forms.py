from django.forms import ModelForm
from .models import DiamondDogList


class DiamondDogListForm(ModelForm):
    class Meta:
        model = DiamondDogList
        fields = '__all__'
