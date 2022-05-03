
from django.forms import ModelForm
from .models import Classes
from django.forms import ModelForm
from .models import djangoClasses

class ClassesForm(ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'

class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = '__all__'
