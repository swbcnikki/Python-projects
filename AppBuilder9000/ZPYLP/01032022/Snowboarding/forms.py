from django.forms import ModelForm
from .models import Ryder


class RyderForm(ModelForm):
    class Meta:
        model = Ryder
        fields = '__all__'
