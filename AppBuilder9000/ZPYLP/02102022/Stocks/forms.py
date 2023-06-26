from django.forms import ModelForm
from .models import Stocks


class StocksForm(ModelForm):
    class Meta:
        model = Stocks
        fields = '__all__'

