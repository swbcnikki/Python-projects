from django.forms import ModelForm
from .models import Choice


class ChooseForm(ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
