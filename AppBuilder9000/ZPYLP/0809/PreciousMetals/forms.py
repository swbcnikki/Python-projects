from django.forms import ModelForm
from .models import PreciousMetalsItem


# Metal Form all fields

class MetalForm(ModelForm):
    class Meta:
        model = PreciousMetalsItem
        fields = '__all__'
