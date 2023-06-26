from django.forms import ModelForm
from .models import Review


# Creates regular Django form that auto-generates view fields for Review submission form
# Form automatically generates based on content of the Meta class
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'