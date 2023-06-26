from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayersForm
from .models import Players
from bs4 import BeautifulSoup
import json
import requests

# Create your views here.



def footballstatshome(request):
    return render(request, "FootballStats/Football_Stats_home.html")



def add_player_stats(request):
    form = PlayersForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('football_stats_home')
    context = {'form': form}
    return render(request, 'FootballStats/football_stats_create.html', context)



def stats(request):
    player_list = Players.Player.all()
    context = {'player_list': player_list}
    return render(request, 'FootballStats/Football_Stats_stats.html', context)


def player_details(request, pk):
    details = get_object_or_404(Players, pk=pk)
    context = {'details': details}
    return render(request, 'FootballStats/Football_Stats_details.html', context)


def player_edit(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('football_stats')
    context = {'form': form}
    return render(request, 'FootballStats/Football_Stats_edit.html', context)


def player_delete(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('football_stats')
    return render(request, 'FootballStats/Football_Stats_delete.html', {'item': item, 'form': form})

"""
==============================================================================================
BEAUTIFUL SOUP SECTION
==============================================================================================
"""


def superbowl_history_scraping(request):
    winner_list = []
    page = requests.get("https://i80sportsblog.com/list-of-super-bowl-winners-and-losers/")
    soup = BeautifulSoup(page.content, 'html.parser')
    previous_winners = soup.find('table')
    winners = previous_winners.find_all('tr')[1:]
    for tr in winners:
        td = tr.find_all('td')
        row = [i.text for i in td]
        cells = row
        winner_list.append(cells)
    print(winner_list)
    context = {'winner_list': winner_list}
    return render(request, 'FootballStats/Football_Stats_SuperBowl_History.html', context)


"""
==============================================================================================
API SECTION
==============================================================================================
"""



def stats_page(request):
    team_names = []
    team_passing_yards = []
    team_tds = []
    url = "https://nfl-team-stats.p.rapidapi.com/v1/nfl-stats/teams/passing-stats/offense/2021"

    headers = {
        'x-rapidapi-host': "nfl-team-stats.p.rapidapi.com",
        'x-rapidapi-key': "97875e5a14mshc10839041a1bef6p1b85f4jsnc165a9e70c87"
    }

    response = requests.request("GET", url, headers=headers)
    teams = json.loads(response.text)
    for i in teams:
        names = i['name']
        team_names.append(names)
    for a in teams:
        passing_yards = a['passYards']
        team_passing_yards.append(passing_yards)
    for x in teams:
        passing_tds = x['touchdowns']
        team_tds.append(passing_tds)

    print(team_names)
    print(team_passing_yards)
    print(team_tds)

    return render(request, 'FootballStats/Football_Stats_team_stats.html')




#Search function to be completed later
#def search(request):
    #player_list = Players.Player.all()
    #context = {'player_list': player_list}




