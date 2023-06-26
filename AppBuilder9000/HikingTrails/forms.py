from django.forms import ModelForm
from .models import Trails


class TrailsForm(ModelForm):
    class Meta:
        model = Trails
        fields = '__all__'
