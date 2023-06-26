from django.forms import ModelForm
from .models import CultClassics

class CultClassicsForm(ModelForm):
    class Meta:
        model = CultClassics
        fields = '__all__'