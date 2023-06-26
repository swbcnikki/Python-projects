from django.forms import ModelForm
from .models import Pokemon


# this will connect with our models.py so like for the type, name, and etc. These will all become a field
# on the website where the user will put in the information and then with this productForm class we can get all
# that information at once and then get what we need from it
class PokemonForm(ModelForm):

    class Meta:
        model = Pokemon
        fields = '__all__'


