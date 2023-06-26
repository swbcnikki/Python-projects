from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import SongForm, PlaylistForm
from . models import Song, Playlist
import requests
import json
from bs4 import BeautifulSoup


#this is the view for the all songs page.
def at_all_songs(request):
    # use the object manager to retrieve all items for display
    songs = Song.Songs.all()
    playlists = Playlist.Playlists.all()
    # add items to dictionary to send to template
    content = {
        'songs': songs,
        'playlists': playlists,
    }
    return render(request, 'ArtistTrack_allSongs.html', content)


# this view uses beautiful soup to get the descriptive paragraphs from the artist wikipedia page.
def at_artist_info(request, pk):
    pk = int(pk)
    song = get_object_or_404(Song, pk=pk)
    artist = song.artist
    while True:
        try:
            response = requests.get("https://en.wikipedia.org/wiki/{}".format(artist), timeout=20)
            soup = BeautifulSoup(response.content, features="html.parser")
            # gets the first three paragraphs of the artist page from wikipedia, which contain the general description.
            html_string = soup.find_all('p')[0]
            html_string2 = soup.find_all('p')[1]
            html_string3 = soup.find_all('p')[2]
            # returns the plain text of the html string
            band_info = html_string.text
            band_info2 = html_string2.text
            band_info3 = html_string3.text
            content = {
                'song': song,
                'band_info': band_info,
                'band_info2': band_info2,
                'band_info3': band_info3
            }
            return render(request, 'ArtistTrack_artistInfo.html', content)
        except:
            # send the message into the dictionary as band info
            band_info = 'Something went wrong. Most likely either the artist name was spelled wrong, ' \
                        'or wikipedia does not have a page for this artist.'
            content = {
                'song': song,
                'band_info': band_info
            }
            return render(request, 'ArtistTrack_artistInfo.html', content)


# this view uses lyrics.ovh, a lyrics API, to get the lyrics of a song by artist and title
def at_lyrics_api(request, pk):
    pk = int(pk)
    song = get_object_or_404(Song, pk=pk)
    # api takes artist and title as parameters
    artist = song.artist
    title = song.song_name
    if song.lyrics is None:
        while True:
            try:
                # set timeout to 20, after this point, it's likely not going to find the song
                response = requests.get("https://api.lyrics.ovh/v1/{}/{}".format(artist, title), timeout=20)
                json_data = json.loads(response.content)
                lyrics = json_data['lyrics']
                song.lyrics = lyrics
                song.save()
                context = {
                    'song': song,
                    'lyrics': lyrics,
                }
                return render(request, "ArtistTrack_lyrics.html", context)
            # set to catch all exceptions, initially tried TimeoutError, it was not catching it.
            except:
                # send this message in as lyrics, when the page renders, it will print the message in place of the lyrics.
                lyrics = 'No Lyrics Found. Try checking spelling, lyrics may not be available for all songs.'
                context = {
                    # I still pass in song, because it is used in the header.
                    'song': song,
                    'lyrics': lyrics,
                }
                return render(request, "ArtistTrack_lyrics.html", context)
    # if the templates already has lyrics for the given song, print the lyrics from the templates.
    else:
        lyrics = song.lyrics
        context = {
            'song': song,
            'lyrics': lyrics,
        }
        return render(request, "ArtistTrack_lyrics.html", context)


def at_playlist_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Playlist, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('at_library')
    context = {'item': item}
    return render(request, "ArtistTrack_deletePlaylist.html", context)


def at_playlist_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Playlist, pk=pk)
    form = PlaylistForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('at_library')
        else:
            print(form.errors)
    else:
        return render(request, 'ArtistTrack_playlistDetails.html', {'form': form})


def at_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('at_library')
    context = {'item': item}
    return render(request, "ArtistTrack_deleteSong.html", context)


def at_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Song, pk=pk)
    form = SongForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('at_library')
        else:
            print(form.errors)
    else:
        return render(request, 'ArtistTrack_details.html', {'form': form})


def at_library(request):
    songs = Song.Songs.all()
    playlists = Playlist.Playlists.all()
    content = {
        'songs': songs,
        'playlists': playlists,
    }
    return render(request, 'ArtistTrack_library.html', content)


def at_home(request):
    return render(request, 'ArtistTrack_home.html')


def add_song(request):
    form = SongForm(data=request.POST or None)
    # When the page is rendered from the library page, it will be as a GET request,
    # When the form is submitted, it will be as a POST request.
    if request.method == 'POST':
        if form.is_valid():
            # gets the song name that was entered by the user and stores it to use in message.
            song_name = form.cleaned_data.get('song_name')
            # saves information provided by the user to the templates
            form.save()
            # adds a message to the page.
            messages.add_message(request, messages.SUCCESS,  'Song "{}" Saved To Library'.format(song_name))
            return redirect('add_song')
    content = {'form': form}
    return render(request, 'ArtistTrack_addSong.html', content)


def add_playlist(request):
    form = PlaylistForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # gets the playlist that was recently inputted and stores it for the message
            playlist_name = form.cleaned_data.get('playlist_name')
            form.save()
            # adds a message to the page.
            messages.add_message(request, messages.SUCCESS, 'Playlist "{}" Saved to Library'.format(playlist_name))
            return redirect('add_playlist')
    content = {'form': form}
    return render(request, 'ArtistTrack_addPlaylist.html', content)
