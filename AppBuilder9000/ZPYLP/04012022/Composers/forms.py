from django.forms import ModelForm
from .models import Composer


class ComposerForm(ModelForm):
    class Meta:
        model = Composer
        fields = '__all__'
