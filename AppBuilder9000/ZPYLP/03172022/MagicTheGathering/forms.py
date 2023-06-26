from django.forms import ModelForm
from .models import Card, Collection

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'