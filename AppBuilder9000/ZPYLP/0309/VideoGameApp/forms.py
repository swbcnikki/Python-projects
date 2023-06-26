from django.forms import ModelForm
from .models import VideoGames


class VideoGamesForm(ModelForm):
    class Meta:
        model = VideoGames
        fields = '__all__'
