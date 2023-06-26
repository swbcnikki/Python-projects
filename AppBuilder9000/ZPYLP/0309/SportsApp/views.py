from django.shortcuts import render, get_object_or_404, redirect
from .models import SavedNbaGame
from .models import FavPlayer
from .forms import NbaGameForm
from .forms import FavPlayerForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests
from bs4 import BeautifulSoup



# Create your views here.


# Creating a Fx to render home page
def home(request):
    return render(request, 'SportsApp/SportsApp_home.html')


# Create CRUD Functionality for adding NBA game to watchlist
def add_nba_game(request):
    form = NbaGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_nba_game')
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, 'SportsApp/SportsApp_create.html', context)


# Create CRUD Functionality for Adding new favorite player

def add_fav_player(request):
    form = FavPlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_fav_player')
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, 'SportsApp/SportsApp_addFavPlayer.html', context)


# Creating a function to get all the items from dB and send it to musicfiles_home.html template

def add_game_archive(request):
    game_list = SavedNbaGame.SavedNbaGame.order_by('date_game').all()
    page = request.GET.get('page', 1)

    paginator = Paginator(game_list, 5)
    try:
        game_list = paginator.page(page)
    except PageNotAnInteger:
        game_list = paginator.page(1)
    except EmptyPage:
        game_list = paginator.page(paginator.num_pages)
    return render(request, 'SportsApp/SportsApp_index.html', {'game_list': game_list})

# Creating a function to get all the item from dB and send it to favArchive.html


def add_fav_archive(request):
    fav_list = FavPlayer.FavPlayer.order_by('fav_player').all()
    page = request.GET.get('page', 1)

    paginator = Paginator(fav_list, 5)
    try:
        fav_list = paginator.page(page)
    except PageNotAnInteger:
        fav_list = paginator.page(1)
    except EmptyPage:
        fav_list = paginator.page(paginator.num_pages)
    return render(request, 'SportsApp/SportsApp_favArchive.html', {'fav_list': fav_list})


# Creating a function to get just one item from the dB and render it on get.html template
def game_details(request, pk):
    pk = int(pk)
    game = get_object_or_404(SavedNbaGame, pk=pk)
    return render(request, 'SportsApp/SportsApp_details.html', {'game': game})


# Creating CRUD function to edit(update) a single item in dB(SavedNbaGame)
def edit_game(request, pk):
    pk = int(pk)
    game = get_object_or_404(SavedNbaGame, pk=pk)
    form = NbaGameForm(data=request.POST or None, instance=game)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('../game_details/')
        else:
            print(form.errors)
    else:
        return render(request, 'SportsApp/SportsApp_edit.html', {'game': game, 'form': form})


# Creating a CRUD Fx to delete a single item in db
def delete_game(request, pk):
    pk = int(pk)
    game = get_object_or_404(SavedNbaGame, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('add_game_archive')
    return render(request, 'SportsApp/SportsApp_delete.html', {"game": game})


# Creating a Fx to confirm the user wants to delete
def confirm_delete(request):
    if request.method == 'POST':
        form = NbaGameForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('add_game_archive')
    else:
        return redirect('add_game_archive')


# Beautiful Soup
def nba_standings(request):
    page = requests.get("https://www.basketball-reference.com/leagues/NBA_2021.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    east_conf_table = soup.find(id="confs_standings_E")
    west_conf_table = soup.find(id="confs_standings_W")
    east_teams_standings = east_conf_table.find_all(class_='full_table')
    west_teams_standings = west_conf_table.find_all(class_='full_table')
    easts_list = []
    wests_list = []
    for team in east_teams_standings:
        east_team_name = team.find(class_='left').get_text()
        east_team_wins = team.find_all(class_='right')[0].get_text()
        east_team_losses = team.find_all(class_='right')[1].get_text()
        east_team_win_loss_pct = team.find_all(class_='right')[2].get_text()
        east_team_games_back = team.find_all(class_='right')[3].get_text()
        east_team_pts_per_game = team.find_all(class_='right')[4].get_text()
        east_team_opp_pts_per_game = team.find_all(class_='right')[5].get_text()
        print(east_team_name, east_team_wins, east_team_losses, east_team_win_loss_pct, east_team_games_back,
              east_team_pts_per_game, east_team_opp_pts_per_game)

        east_team_dict = {
            'east_team_name': east_team_name,
            'east_team_wins': east_team_wins,
            'east_team_losses': east_team_losses,
            'east_team_win_loss_pct': east_team_win_loss_pct,
            'east_team_games_back': east_team_games_back,
            'east_team_pts_per_game': east_team_pts_per_game,
            'east_team_opp_pts_per_game': east_team_opp_pts_per_game,
            }
        easts_list.append(east_team_dict)

    for team in west_teams_standings:
        west_team_name = team.find(class_='left').get_text()
        west_team_wins = team.find_all(class_='right')[0].get_text()
        west_team_losses = team.find_all(class_='right')[1].get_text()
        west_team_win_loss_pct = team.find_all(class_='right')[2].get_text()
        west_team_games_back = team.find_all(class_='right')[3].get_text()
        west_team_pts_per_game = team.find_all(class_='right')[4].get_text()
        west_team_opp_pts_per_game = team.find_all(class_='right')[5].get_text()
        print(west_team_name, west_team_wins, west_team_losses, west_team_win_loss_pct, west_team_games_back,
              west_team_pts_per_game, west_team_opp_pts_per_game)

        west_team_dict = {
            'west_team_name': west_team_name,
            'west_team_wins': west_team_wins,
            'west_team_losses': west_team_losses,
            'west_team_win_loss_pct': west_team_win_loss_pct,
            'west_team_games_back': west_team_games_back,
            'west_team_pts_per_game': west_team_pts_per_game,
            'west_team_opp_pts_per_game': west_team_opp_pts_per_game,
        }
        wests_list.append(west_team_dict)

    context = {'easts_list': easts_list, 'wests_list': wests_list}
    return render(request, 'SportsApp/SportsApp_standings.html', context)





