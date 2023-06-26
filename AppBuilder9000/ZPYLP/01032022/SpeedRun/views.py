from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SpeedrunForm
from .game_forms import GameForm
from .models import Record, GameName
import requests
import json
import http.client


# render home page
def speed_run_home(request):
    return render(request, "speed_run_home.html")


# create speedrun record form using model form in django
def add_record(request):
    form = SpeedrunForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('speed_run_home')
    else:
        print(form.errors)
        form = SpeedrunForm()
        context = {'form': form}
    return render(request, 'speed_run_create.html', context)


# create game form using model form in django
def add_game(request):
    form = GameForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('speed_run_create')
    else:
        print(form.errors)
        form = GameForm()
        context = {'form': form}
    return render(request, 'speed_run_create_game.html', context)


# displays a list of all games entered as GameName Objects
def all_games(request):
    games = GameName.objects.all()
    return render(request, 'speed_run_all_games.html', {'games': games})


# passes Record information if player has a record for the selected game
def game_record(request, pk):
    gamename = get_object_or_404(GameName, pk=pk)
    records = Record.objects.filter(game=gamename).order_by("time")
    content = {'gamename': gamename, 'records': records}
    return render(request, 'speed_run_game_records.html', content)


# displays all details relevant to a selected player
def speed_run_details(request, pk):
    details = get_object_or_404(Record, pk=pk)
    content = {'details': details}
    return render(request, 'speed_run_details.html', content)


# allows the user to edit an entry
def speed_run_edit(request, pk):
    item = get_object_or_404(Record, pk=pk)
    form = SpeedrunForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('speed_run_all_games')
        else:
            print(form.errors)
    else:
        return render(request, 'speed_run_edit.html', {'form': form, 'item': item})


# allows users to delete a record
def speed_run_delete(request, pk):
    item = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('speed_run_all_games')
    context = {'item': item}
    return render(request, 'speed_run_delete.html', context)


def speed_run_api(request):

    search_list = []

    if request.method == 'POST':

        url = "https://rawg-video-games-database.p.rapidapi.com/games?key=5f37df7ee53e491f847a43dfa97cb3a2"

        headers = {
            'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com",
            'x-rapidapi-key': "9afece8438msh5f25fff510a60bbp1954d2jsn7f98f53b6d37"
        }

        params = {"search": request.POST['searchItem']}

        response = requests.request("GET", url, headers=headers, params=params)

        game_data = json.loads(response.text)

        for game in game_data['results']:
            bg_img = game['background_image']
            title = game['name']
            release = game['released']
            rating = game['rating']
            game_array = (bg_img, title, release, rating)
            search_list.append(game_array)

    content = {
        'search_list': search_list
    }

    return render(request, 'speed_run_api.html', content)


