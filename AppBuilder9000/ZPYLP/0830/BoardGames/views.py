from html import unescape
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import BoardGame
from .forms import BoardGameForm
import requests
import xml.etree.ElementTree as ET

def BoardGames_home(request):
    boardgames = BoardGame.objects.all()
    return render(request, 'BoardGames/musicfiles_home.html', {'boardGames': boardgames})


def BoardGames_get(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    boardgame.Description = unescape(boardgame.Description)
    return render(request, 'BoardGames/get.html', {'b': boardgame})


def BoardGames_create(request):
    form = BoardGameForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('BoardGames_get', pk=result.id)
    else:
        return render(request, 'BoardGames/create.html', {'form': form})


def BoardGames_edit(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    form = BoardGameForm(request.POST or None, instance=boardgame)
    if request.POST and form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return render(request, 'Boardgames/get.html', {'b': boardgame})
    else:
        context = {'form': form,
                   'id': boardgame.pk,
                   'error': 'The form was not updated successfully. Please enter valid information.'}
        return render(request, 'BoardGames/edit.html', context)


def BoardGames_delete(request, pk):
    BoardGame.objects.filter(id=pk).delete()
    boardgames = BoardGame.objects.all()
    return render(request, 'BoardGames/musicfiles_home.html', {'boardGames': boardgames})


def BoardGames_favorite(request, pk):
    if request.method == "POST":
        pk = request.POST.get("id")
        boardgame = BoardGame.objects.get(id=pk)
        boardgame.Favorite = not boardgame.Favorite
        boardgame.save()
        data = { "msg": "Favorite toggled.", 'value': boardgame.Favorite, 'id': pk, }
        return JsonResponse(data)
    else:
        data = { "msg": "Message received!", 'value': boardgame.Favorite, 'id': pk, }

def BoardGames_seed(request):
    boardgames = BoardGame.objects.all()
    if len(boardgames) == 0:
        gameIdsList = [317985, 9209, 2651, 167791, 36218, 68448, 286062, 3955, 1198, 36345, 148228, 822, 97903, 30549, 204583, 161417, 63888, 1293, 16992, 180974, 173346, 3076, 312484]
        gameIds = ",".join(str(x) for x in gameIdsList)
        url = 'https://api.geekdo.com/xmlapi2/thing?thing=boardgame&id=' + gameIds
        for item in ET.fromstring(requests.get(url).content):
            BoardGame.objects.create(
                Name = item.find('name').attrib['value'],
                Publisher = item.find('link[@type="boardgamepublisher"]').attrib['value'],
                Year = item.find('yearpublished').attrib['value'],
                Description = item.find('description').text,
                Thumbnail = item.find('thumbnail').text,
                Image = item.find('image').text
            )
    return redirect('BoardGames_home')
