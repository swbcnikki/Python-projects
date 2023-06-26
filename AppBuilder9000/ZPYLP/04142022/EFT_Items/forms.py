from django.forms import ModelForm
from .models import EFTItems


class EFTForm(ModelForm):
    class Meta:
        model = EFTItems
        fields = '__all__'
