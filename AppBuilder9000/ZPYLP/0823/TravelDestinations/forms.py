from django.forms import ModelForm
from .models import destination

class DestinationForm(ModelForm):
    class Meta:
        model = destination
        fields = '__all__'
