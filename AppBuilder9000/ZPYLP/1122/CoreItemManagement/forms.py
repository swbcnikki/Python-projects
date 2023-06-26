from django.forms import ModelForm
from .models import Item, Vendor


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

