from django.forms import ModelForm
from .models import Games, Dlc, Wishlist

class GameForm(ModelForm):
    class Meta:
        model = Games
        fields = '__all__'

class DlcForm(ModelForm):
    class Meta:
        model = Dlc
        fields = '__all__'

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'

