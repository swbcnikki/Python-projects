from django.forms import ModelForm
from django import forms
from .models import Restaurant, Dish


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class DishForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Dish
        fields = '__all__'


class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=100)


