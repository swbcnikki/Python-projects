from django.forms import ModelForm
from .models import MyShows


class ShowForm(ModelForm):
    class Meta:
        model = MyShows
        fields = '__all__'
