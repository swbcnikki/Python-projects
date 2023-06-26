from django.forms import ModelForm
from .models import ReviewTrail


class TrailReviewForm(ModelForm):
    class Meta:
        model = ReviewTrail
        fields = '__all__'