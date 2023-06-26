from django.forms import ModelForm
from .models import Convert


class ConvertForm(ModelForm):
    class Meta:
        model = Convert
        fields = '__all__'
