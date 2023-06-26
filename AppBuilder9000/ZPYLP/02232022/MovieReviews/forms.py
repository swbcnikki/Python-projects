from django.forms import ModelForm
from .models import Movies


# This model Form is based on the Movie model class
class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'


