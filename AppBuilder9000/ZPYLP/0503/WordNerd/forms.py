from django.forms import ModelForm
from .models import word
#ModelForm based of wordform mode
class wordform(ModelForm):
    class Meta:
        model = word
        fields = '__all__'

