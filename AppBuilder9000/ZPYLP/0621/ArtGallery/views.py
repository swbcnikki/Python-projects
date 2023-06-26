from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtistForm
from .models import Artist


def home(request):
    return render(request, 'ArtGallery_home.html')

def apply(request):
    form = ArtistForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("ArtGallery_home")
    return render(request, 'ArtGallery_login.html', {'form': form})

def users(request):
    user_display = Artist.Artists.all()
    context = {'user_display': user_display}
    return render(request, 'ArtGallery_users.html', context)

def user_details(request, pk):
    details = get_object_or_404(Artist, pk=pk)
    context = {'details': details}
    return render(request, 'ArtGallery_details.html', context)

