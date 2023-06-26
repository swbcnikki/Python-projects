from django.forms import ModelForm
from .models import StockData


class StockForm(ModelForm):
    class Meta:
        model = StockData
        fields = ['StockCompanyName', 'StockTicker', 'StockPrice', 'StockAmount']
