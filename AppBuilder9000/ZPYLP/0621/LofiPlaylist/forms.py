from django.forms import ModelForm, TextInput
from .models import Song
from django import forms
import requests


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

#API

class SearchForm(forms.Form):
    artist = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)

    # def search(self):
    #     result = {}
    #     artist = self.cleaned_data['artist']
    #     title = self.cleaned_data['title']
    #     endpoint = 'https://api.lyrics.ovh/v1/{artist}/{title}'
    #     url = endpoint.format(artist_id=artist, title_id=title)
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         result = response.json()
    #         result['success'] = True
    #     else:
    #         result['success'] = False
    #         if response.status_code == 404:
    #             result['message'] = 'No entry found for "%s"' % title
    #         else:
    #             result['message'] = 'The Lyrics Api is not available at the moment'
    #     return result
    #




