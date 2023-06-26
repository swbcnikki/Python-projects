from django.forms import ModelForm
from .models import KeyboardList


class KeyboardListForm(ModelForm):
    class Meta:
        model = KeyboardList
        fields = '__all__'
