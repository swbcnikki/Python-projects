from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import GameForm
from .models import Game
from bs4 import BeautifulSoup
import requests

import http.client










# Displays the home page
def BestGamesEver_Home(request):
    return render(request, 'BestGamesEver/musicfiles_home.html')

#Function for user to create a Db entry
def Game_Create(request):
    form = GameForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect("Game_Create")

    return render(request, 'BestGamesEver/Gamecreate.html', {"form": form})

# Function to retrieve all items from our Db
def Game_View(request):
    #gets all objects of the Game database unsorted
    game_list = Game.objects.all()

    return render(request, 'BestGamesEver/ViewGames.html', {'game_list': game_list})


# Function to allow user to view a single item

def Game_Details(request, game_id):
    details = Game.objects.get(id=game_id)
    return render(request, "BestGamesEver/Game_Details.html", {'details': details})

# Function to edit an entry

def Edit_Games(request, game_id):
    item = get_object_or_404(Game, id=game_id)
    form = GameForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("Game_View")
    content = {'form': form}
    return render(request, 'BestGamesEver/Game_Edit.html', content)


# Function to delete an entry
def Delete_Games(request, game_id):
    item = get_object_or_404(Game, id=game_id)
    form = GameForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
            item.delete()
            return redirect("Game_View")
    content = {'form': form}
    return render(request, 'BestGamesEver/Game_Delete.html', {'item': item, 'form': form})


def get_html_content(game):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    game = game.replace(' ', '+')
    html_content = session.get(f'https://www.amazon.com/s?k={game}&ref=nb_sb_noss_2').text
    return html_content


# Beautiful Soup Function
def View_Price(request):
    game_data = None
    if 'game' in request.GET:
        # Fetch game data
        game = request.GET.get('game')
        html_content = get_html_content(game)
        soup = BeautifulSoup(html_content, 'html.parser')
        # Setting our variable to dictionary form
        game_data = {}
        # Will display name of the game and current price
        game_data['title'] = soup.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'}).text
        game_data['price'] = soup.find('span', attrs={'class': 'a-offscreen'}).text

    return render(request, 'BestGamesEver/View_Price.html', {'game': game_data})

# API classes
def api(request):
    conn = http.client.HTTPSConnection("the-legend-of-zelda.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "the-legend-of-zelda.p.rapidapi.com",
        'x-rapidapi-key': "0dc56d5340msh7696d153664dadfp121956jsn1fac11e318d3"
    }

    conn.request("GET", "/items?name=Bow&page=0&limit=5", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(data)
    content={'info':data}

    print(data.decode("utf-8"))
    return render(request, 'BestGamesEver/API.html', content)