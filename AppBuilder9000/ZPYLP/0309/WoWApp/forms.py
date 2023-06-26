from django.forms import ModelForm
from .models import Character, Favorite


class CreateCharacter(ModelForm):
    class Meta:
        #grabbing the model 'Subscriber' and putting it in the variable 'model'
        model = Character
        #all fields from the 'Subscriber' model
        fields = '__all__'


class SaveFavorite(ModelForm):
    class Meta:
        model = Favorite
        fields = '__all__'