from django.forms import ModelForm
from .models import Fighter


class FighterForm(ModelForm):
    class Meta:
        model = Fighter  # use the MuayThai model
        fields = '__all__'
