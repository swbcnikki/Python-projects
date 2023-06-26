from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['AnimeName', 'Genre', 'About', 'Rating', 'Review']


