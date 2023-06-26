from django.forms import ModelForm
from .models import celestialObjects


class form_addObject(ModelForm):
    class Meta:
        model = celestialObjects
        fields = '__all__'