from django.forms import ModelForm
from .models import Description


class DescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = '__all__'
