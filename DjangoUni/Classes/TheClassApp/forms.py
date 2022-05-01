
from django.forms import ModelForm
from .models import Classes

class ClassesForm(ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'