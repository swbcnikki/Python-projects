from django.forms import ModelForm
from .models import Account, Product

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'