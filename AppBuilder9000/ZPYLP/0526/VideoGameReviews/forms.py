from django import forms
from .models import VideoReviews


class VideoReviewsForm(forms.ModelForm):
    class Meta:
        model = VideoReviews
        fields = ['GameName', 'GameGenre', 'GameReview', 'GameRating']
        widgets = {
            'GameName': forms.TextInput(attrs={'class': 'form-control'}),
            'GameGenre': forms.TextInput(attrs={'class': 'form-control'}),
            'GameReview': forms.Textarea(attrs={'class': 'form-control'})
        }
