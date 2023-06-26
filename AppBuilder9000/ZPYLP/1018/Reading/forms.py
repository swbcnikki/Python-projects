from django.forms import ModelForm
from .models import Archive

class RecordForm(ModelForm):
    class Meta:
        model = Archive
        fields = '__all__'