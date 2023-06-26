from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album


def home(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    print(albums)
    return render(request, 'AlbumTracker/AlbumTracker_home.html', context)


def add_album(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('AlbumTracker_add')
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, 'AlbumTracker/AlbumTracker_add.html', context)


def details(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'AlbumTracker/AlbumTracker_details.html', context)