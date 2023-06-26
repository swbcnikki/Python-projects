from django.forms import ModelForm
from .models import Neighborhood, Review

class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


