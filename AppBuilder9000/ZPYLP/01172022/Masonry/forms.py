from django.forms import ModelForm
from .models import Quotes


class QuoteForm(ModelForm):
    class Meta:
        model = Quotes
        fields = '__all__'

