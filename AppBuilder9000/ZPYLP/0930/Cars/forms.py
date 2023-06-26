from django.forms import ModelForm
from .models import description

class descriptionForm(ModelForm):
    class Meta:
        model = description
        fields = '__all__'