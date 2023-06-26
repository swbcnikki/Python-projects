from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from .forms import RaceHorseForm
from .models import RaceHorse


def home(request):
    return render(request, "HorseApp/HorseApp_Home.html")

# view for racehorse form, allows user input to create/save new horses


def addhorse(request):
    form = RaceHorseForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('HorseApp_Add_Horse')
        else:
            print(form.errors)
            form = RaceHorseForm()
    content = {'form': form}
    return render(request, "HorseApp/HorseApp_Add_Horse.html", content)


def horseindex(request):
    search_horseindex = RaceHorse.RaceHorses.all()
    query = request.GET.get('q')
    if query:
        search_horseindex = RaceHorse.RaceHorses.filter(
            Q(horse_name__icontains=query)
        ).distinct()

    paginator = Paginator(search_horseindex, 1)
    page = request.GET.get('page')
    try:
        racehorses = paginator.page(page)
    except PageNotAnInteger:
        racehorses = paginator.page(1)
    except EmptyPage:
        racehorses = paginator.page(paginator.num_pages)

    context = {'horse_index_list': racehorses,
               'search_horseindex': search_horseindex}
    return render(request, 'HorseApp/HorseApp_Index.html', context)
