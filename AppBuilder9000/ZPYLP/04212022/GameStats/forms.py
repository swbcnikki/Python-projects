from django.forms import ModelForm
from .models import Games, Publishers

class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = '__all__'
        exclude = ('publisher',)

class PublishersForm(ModelForm):
    class Meta:
        model = Publishers
        fields = '__all__'


