from django.forms import ModelForm
from django import forms
from .models import Song, Playlist


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('song_name', 'artist', 'album', 'genre', 'year')
        #allows me to use bootstrap to style the form
        widgets = {
            'song_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Song Name'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Artist'}),
            'album': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Album'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
        }


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'

        widgets = {
            'playlist_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Playlist Name'}),
            'playlist_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'a description about your playlist'}),
            'playlist_songs': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
