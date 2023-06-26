from django import forms
from django.forms import ModelForm
from .models import Cocktail, Review, rating_choices


class CocktailForm(ModelForm):
    # photo = forms.FileField()

    class Meta:
        model = Cocktail
        exclude = ['avg_rating']


class ReviewForm(ModelForm):
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=rating_choices)

    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comments']
