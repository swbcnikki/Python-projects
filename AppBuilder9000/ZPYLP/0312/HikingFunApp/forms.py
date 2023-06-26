from django.forms import ModelForm
from .models import Trails


class NewTrailForm(ModelForm):
    class Meta:
        model = Trails
        fields = '__all__'

