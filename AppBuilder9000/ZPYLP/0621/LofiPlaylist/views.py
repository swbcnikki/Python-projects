from django.shortcuts import render, redirect, get_object_or_404
from .forms import SongForm, SearchForm
from .models import Song
import requests

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .lofi_serializer import SongSerializer




def lofi_home(request):
    return render(request, 'lofi_home.html',)


def lofi_add(request):
    form = SongForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lofi_display')
    return render(request, 'lofi_add.html', {'form': form})


def lofi_display(request):
    LofiPlaylist = Song.objects.all()
    return render(request, 'lofi_display.html', {'LofiPlaylist': LofiPlaylist})


def lofi_details(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'lofi_details.html', {'song': song})


def lofi_edit(request, pk):
    song = get_object_or_404(Song, pk=pk)
    form = SongForm(request.POST or None, instance=song)
    if form.is_valid():
        form.save()
        return redirect('lofi_display')
    return render(request, 'lofi_edit.html', {'form': form})


def confirm_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('lofi_display')
    return render(request, 'confirm_delete.html', {'song': song})

# My Created API in Django Rest framework http://127.0.0.1:8000/LofiPlaylist/songs/

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]


# consume lyrics API

# def lofi_lyrics(request):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         song_lyrics = ""
#         print(f"FORM IS VALID{form.is_valid()}")
#         if form.is_valid():
#             print(f"Form Data {form.cleaned_data}")
#             artist = form.cleaned_data['artist']
#             title = form.cleaned_data['title']
#             response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
#             song = response.json()
#             song_lyrics = song['lyrics']
#         return render(request, 'lofi_lyrics.html', {
#             'lyrics': song_lyrics
#         })


def lofi_lyrics(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        song_lyrics = ""
        print(f"FORM IS VALID{form.is_valid()}")
        if form.is_valid():
            print(f"Form Data {form.cleaned_data}")
            artist = form.cleaned_data['artist']
            title = form.cleaned_data['title']
            try:
                response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
                response.raise_for_status()
                song = response.json()
                song_lyrics = song['lyrics']
            except requests.exceptions.RequestException as e:
                print(e)
        return render(request, 'lofi_lyrics.html', {
            'lyrics': song_lyrics
        })




