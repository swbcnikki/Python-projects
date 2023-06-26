from django.forms import ModelForm
from .models import Charts

class ChartsForm(ModelForm):
    class Meta:
        model = Charts
        fields = '__all__'
