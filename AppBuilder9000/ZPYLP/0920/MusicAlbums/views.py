from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
# Create your views here.
def MusicAlbums_home(request):
    return render(request, 'MusicAlbums/MusicAlbums_home.html')

def MusicAlbums_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MusicAlbums_add')
        else:
            form = AlbumForm(request.POST)
            return render(request, 'MusicAlbums/MusicAlbums_add.html',
                          {'form': form})
    else:
        form = AlbumForm(None)
        return render(request, 'MusicAlbums/MusicAlbums_add.html', {'form': form})

def MusicAlbums_display(request):
    all_albums = Album.objects.all
    return render(request, 'MusicAlbums/MusicAlbums_display.html', {'all': all_albums})

def MusicAlbums_details(request, pk):
    music_details = get_object_or_404(Album, pk=pk)
    content = {'music_details': music_details}
    return render(request, 'MusicAlbums/MusicAlbums_details.html', content)