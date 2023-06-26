from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicalArtistsForm, SongNamesForm, AlbumNamesForms
from .models import MusicalArtists, SongNames, AlbumNames
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bs4 import BeautifulSoup as bs
import requests




# Render Home Page
def home(request):
    return render(request, 'MusicApp/MusicApp_home.html')


# Render Create Artist Entry Page
def MusicApp_create_artist(request):
    form = MusicalArtistsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MusicApp_home')
    else:
        form = MusicalArtistsForm()
    context = {
        'form': form
    }
    return render(request, 'MusicApp/MusicApp_create_artist.html', context)


# Render Create Song Entry Page
def MusicApp_create_song(request):
    form = SongNamesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MusicApp_home')
    else:
        form = SongNamesForm()
    context = {
        'form': form
    }
    return render(request, 'MusicApp/MusicApp_create_song.html', context)


# Render Create Album Entry Page
def MusicApp_create_album(request):
    form = AlbumNamesForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MusicApp_home')
    else:
        form = AlbumNamesForms()
    context = {
        'form': form
    }
    return render(request, 'MusicApp/MusicApp_create_album.html', context)


# Render Artist Index Page
def artist_index(request):
    artist_list = MusicalArtists.objects.order_by('artist_name').all()
    page = request.GET.get('page', 1)
    # show 10 artists per page
    paginator = Paginator(artist_list, 10)
    try:
        artists = paginator.page(page)
    except PageNotAnInteger:
        artists = paginator.page(1)
    except EmptyPage:
        artists = paginator.page(paginator.num_pages)
    return render(request, 'MusicApp/MusicApp_artist_index.html', {'artists': artists})


# Render Song Index Page
def song_index(request):
    song_list = SongNames.objects.order_by('song_name').all()
    page = request.GET.get('page', 1)
    # show 10 songs per page
    paginator = Paginator(song_list, 10)
    try:
        songs = paginator.page(page)
    except PageNotAnInteger:
        songs = paginator.page(1)
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)
    return render(request, 'MusicApp/MusicApp_song_index.html', {'songs': songs})


# Render Album Index Page
def album_index(request):
    album_list = AlbumNames.objects.order_by('album_name').all()
    page = request.GET.get('page', 1)
    # show 10 albums per page
    paginator = Paginator(album_list, 10)
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)
    return render(request, 'MusicApp/MusicApp_album_index.html', {'albums': albums})


# Render Search Results from artist search
def artist_search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            # Allow to look up by artist name only
            lookups = Q(artist_name__icontains=query)

            results = MusicalArtists.objects.order_by('artist_name').filter(
                # distinct() is used to avoid duplicate results
                lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'MusicApp/MusicApp_artist_search_results.html', context)

        else:
            return render(request, 'MusicApp/MusicApp_artist_search_results.html')

    else:
        return render(request, 'MusicApp/MusicApp_artist_search_results.html')


# Render Search Results from song search
def song_search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            # Allow to look up by song name only
            lookups = Q(song_name__icontains=query)

            results = SongNames.objects.order_by('song_name').filter(
                # distinct() is used to avoid duplicate results
                lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'MusicApp/MusicApp_song_search_results.html', context)

        else:
            return render(request, 'MusicApp/MusicApp_song_search_results.html')

    else:
        return render(request, 'MusicApp/MusicApp_song_search_results.html')


# Render Search Results from album search
def album_search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            # Allow to look up by album name and artist name only
            lookups = Q(album_name__icontains=query) | Q(artist_name__icontains=query)

            results = AlbumNames.objects.order_by('album_name').filter(
                # distinct() is used to avoid duplicate results
                lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'MusicApp/MusicApp_album_search_results.html', context)

        else:
            return render(request, 'MusicApp/MusicApp_album_search_results.html')

    else:
        return render(request, 'MusicApp/MusicApp_album_search_results.html')



# Artist Details Page
def artist_details(request, pk):
    artists = get_object_or_404(MusicalArtists, pk=int(pk))
    return render(request, 'MusicApp/MusicApp_artist_details.html', {'artists': artists})


# Song Details Page
def song_details(request, pk):
    songs = get_object_or_404(SongNames, pk=int(pk))
    return render(request, 'MusicApp/MusicApp_song_details.html', {'songs': songs})


# Album Details Page
def album_details(request, pk):
    albums = get_object_or_404(AlbumNames, pk=int(pk))
    return render(request, 'MusicApp/MusicApp_album_details.html', {'albums': albums})


# Edit Artist
def edit_artist(request, pk):
    artists = get_object_or_404(MusicalArtists, pk=int(pk))
    form = MusicalArtistsForm(data=request.POST or None, instance=artists)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('MusicApp_artist_details', pk)
        else:
            print(form.errors)
    else:
        return render(request, 'MusicApp/MusicApp_edit_artist.html', {'artists': artists, 'form': form})


# Edit Song
def edit_song(request, pk):
    songs = get_object_or_404(SongNames, pk=int(pk))
    form = SongNamesForm(data=request.POST or None, instance=songs)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('MusicApp_song_details', pk)
        else:
            print(form.errors)
    else:
        return render(request, "MusicApp/MusicApp_edit_song.html", {'songs': songs, 'form': form})


# Edit Album
def edit_album(request, pk):
    albums = get_object_or_404(AlbumNames, pk=int(pk))
    form = AlbumNamesForms(data=request.POST or None, instance=albums)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('MusicApp_album_details', pk)
        else:
            print(form.errors)
    else:
        return render(request, "MusicApp/MusicApp_edit_album.html", {'albums': albums, 'form': form})


# Delete Artist
def delete_artist(request, pk):
    artists = get_object_or_404(MusicalArtists, pk=int(pk))
    if request.method == 'POST':
        artists.delete()
        return redirect('MusicApp_artist_index')
    return redirect('MusicApp_artist_details', pk)


# Delete Song
def delete_song(request, pk):
    songs = get_object_or_404(SongNames, pk=int(pk))
    if request.method == 'POST':
        songs.delete()
        return redirect('MusicApp_song_index')
    return redirect('MusicApp_song_details', pk)


# Delete Album
def delete_album(request, pk):
    albums = get_object_or_404(AlbumNames, pk=int(pk))
    if request.method == 'POST':
        albums.delete()
        return redirect('MusicApp_album_index')
    return redirect('MusicApp_album_index', pk)


def bs_artist_chart(request):
    r = requests.get('https://www.rollingstone.com/charts/artists/')
    soup = bs(r.content, 'html.parser')
    titles = soup.find_all(class_='c-chart__table--title')
    artist_list = []
    for i in titles:
        paragraphs = i.find_all('p')
        for p in paragraphs:
            artist = p.text
            artist_list.append(artist)
    print(artist_list)
    context = {"artist_list": artist_list}
    return render(request, 'MusicApp/MusicApp_top_artists_chart.html', context)
