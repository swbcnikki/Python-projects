from django.shortcuts import render, redirect, get_object_or_404
from .form import ArtForm
from django.core.paginator import Paginator
from django.db import models
from .models import Art


def home(request):
    return render(request, 'ArtistsApp/ArtistsApp_home.html')

def ArtistsApp_creator(request):
    form = ArtForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ArtistsApp_home')
    context = {'form': form}
    return render(request, "ArtistsApp/ArtistsApp_creator.html", context)


def ArtistsApp_details(request,pk):
    pieces = get_object_or_404(Art, pk=pk)
    get_details = {'pieces': pieces}
    return render(request, "ArtistsApp/ArtistsApp_details.html", get_details)




def index(request):
    pieces = Art.object.all()
    paginator = Paginator(pieces, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "ArtistsApp/ArtistsApp_index.html", {'page_obj': page_obj})





