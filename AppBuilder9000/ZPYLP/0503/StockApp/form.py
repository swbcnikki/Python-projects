from django.forms import ModelForm
from .models import WatchStock


class StockForm(ModelForm):
    class Meta:
        model = WatchStock
        fields = '__all__'


