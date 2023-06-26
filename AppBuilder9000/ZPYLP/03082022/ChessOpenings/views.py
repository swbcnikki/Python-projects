from django.shortcuts import render, redirect, get_object_or_404
from .forms import GamesForm
from .models import Games
from django.contrib import messages
from .lichessAPI import parse_response
from .web_scrape import web_scrape


def homepage(request, pk=0, search=False):
    return render(request, 'ChessOpenings/chess_index.html')


def add_game(request):
    form = GamesForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            test = form.save()
            print(test.title)
            return redirect(homepage)
    return render(request, "ChessOpenings/add_game.html", context)


# Create your views here.
def search_games(request):
    all_entries = Games.Game.all()
    print(all_entries)
    context = {'games': all_entries}
    return render(request, "ChessOpenings/chess_search.html", context)


# Create your views here.
def game_details(request, pk):
    details = get_object_or_404(Games, pk=pk)
    context = {'game': details}
    return render(request, "ChessOpenings/game_details.html", context)


def game_edit(request, pk):
    details = Games.Game.get(id=pk)
    form = GamesForm(request.POST or None, instance=details)

    context = {'form': form,
               'game': details}

    if form.is_valid():
        test = form.save()
        test.save()
        messages.success(request, "You successfully updated the post")

        context = {'form': form,
                   'game': details}

        return render(request, "ChessOpenings/edit.html", context)

    return render(request, "ChessOpenings/edit.html", context)


def delete(pk):
    item = get_object_or_404(Games, pk=pk)
    print(item)

    item.delete()
    return redirect('chess_search')


def api_search(request):
    context = {}
    if request.GET.get('mybtn'):
        games = parse_response(request.GET.get('mytextbox'))
        context = {'games': games}
    return render(request, "ChessOpenings/search_api.html", context)

def opening_scrape(request):
    context = {}
    content = {'info': web_scrape()}
    context['content'] = content
    return render(request, "ChessOpenings/chess_info.html", context)
