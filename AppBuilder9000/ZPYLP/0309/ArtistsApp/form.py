from django.forms import ModelForm
from .models import Art
from django import forms


class ArtForm(ModelForm):
    class Meta:
        model = Art
        widgets = {'date_published': forms.SelectDateWidget(years=range(2021, 1940, -1))}
        fields = '__all__'



