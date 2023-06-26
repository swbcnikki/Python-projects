from django.shortcuts import render, redirect, get_object_or_404
from .models import Description
from .forms import DescriptionForm


def anime_home(request):
    descriptions = Description.objects.all()
    return render(request, 'Anime/Anime_index.html', {'descriptions': descriptions})


def Anime_create(request):
    form = DescriptionForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('Add_Anime')
    else:
        return render(request, 'Anime/Anime_create.html', {'form': form})


def Anime_entries(request):
    entries = Description.objects.all()
    content = {'entries': entries}
    return render(request, 'Anime/Anime_entries.html', content)


def Anime_details(request, pk):
    details = get_object_or_404(Description, pk=pk)
    context = {'details': details}
    return render(request, "Anime/Anime_details.html", context)



