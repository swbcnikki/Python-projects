from django.shortcuts import render, redirect, get_object_or_404
from .models import Defensive_Stats, PlayerDb, FavoritesDB
from .forms import Def_Stats_Form
from bs4 import BeautifulSoup
import requests
import sqlite3


def add_player(request):
    form = Def_Stats_Form(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('display-all')
    content = {'form': form}
    return render(request, 'nba-add-player.html', content)


# ===============================================================================================
#       Display functions to show All players, or players from specific seasons (i.e. 2020-2021)
# ===============================================================================================
def display_all(request):
    players = Defensive_Stats.objects.all()
    content = {'players': players}
    return render(request, 'nba-display.html', content)


def display_2021(request):
    year = '2020-2021'
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-{}.html'.format(year), content)


def display_2020(request):
    year = '2019-2020'
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2019-2020.html', content)


def display_2019(request):
    year = '2018-2019'
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2018-2019.html', content)


def display_favorites(request):
    players = FavoritesDB.objects.all()
    content = {'players': players}
    return render(request, 'nba-favorites.html', content)


# ===============================================================================================
#           Display the details for individual players
# ===============================================================================================
def show_details(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    year = player.year
    name = player.playerName
    rebs = player.defRebs
    steals = player.steals
    blocks = player.blocks
    total_def_points = rebs + (steals * 3) + (blocks * 3)

    content = {'player': player,
               'year': year,
               'playerName': name,
               'defRebs': rebs,
               'steals': steals,
               'blocks': blocks,
               'total_def_points': total_def_points,
               }
    return render(request, 'nba-get.html', content)


# ===============================================================================================
#           EDIT and DELETE player functions
# ===============================================================================================
def delete_player(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    year = player.year
    form = Def_Stats_Form(data=request.POST or None, instance=player)
    if request.method == 'POST':
        player.delete()
        return redirect('display-all')
    content = {'player': player, 'year': year, 'form': form}
    return render(request, 'nba-delete.html', content)


def edit_player(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    form = Def_Stats_Form(data=request.POST or None, instance=player)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('display-all')
    content = {'form': form}
    return render(request, 'nba-edit.html', content)


def remove_favorite(request, pk):
    player = get_object_or_404(FavoritesDB, pk=pk)
    conn = sqlite3.connect('db.sqlite3')
    with conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM NBAstats_FavoritesDB WHERE id = ?', [pk])
    content = {'player': player}
    return render(request, 'nba-delete-favorite.html', content)


# ===============================================================================================
#           SCRAPE DATA AND SAVE TO DATABASE
# ===============================================================================================
def b_ref(request):
    # URL page we will scrape
    brURL = "https://www.basketball-reference.com/leagues/NBA_2021_totals.html"

    page = requests.get(brURL)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Get all Headers from table and put them in a list
    headers = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    # Select only the headers I want and put them in a list
    myHeaders = list(headers[i] for i in [1, 22, 25, 26])

    rows = soup.findAll('tr')[1:]

    # Extract table data (td) from the rows and put into list
    allStats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

    # connect to templates, and clear it so that it's empty
    conn = sqlite3.connect('db.sqlite3')
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM NBAstats_PlayerDb")

    player_dict = []
    check_name = ''
    pk = 1
    for row in allStats:
        if len(row) > 0:  # check to see if list is empty
            playerName = row[0]
            defRebs = int(row[21])
            steals = int(row[24])
            blocks = int(row[25])
            total_def_points = defRebs + (steals * 3) + (blocks * 3)
            if total_def_points >= 200:
                if playerName != check_name:
                    myStats = {'playerName': playerName,
                               'defRebs': defRebs,
                               'steals': steals,
                               'blocks': blocks,
                               'total_def_points': total_def_points,
                               'pk': pk}
                    player_dict.append(myStats)

                    conn = sqlite3.connect('db.sqlite3')
                    with conn:
                        cur = conn.cursor()
                        cur.execute('INSERT INTO NBAstats_PlayerDb VALUES (?,?,?,?,?,?)',
                                    [pk, playerName, defRebs, steals, blocks, total_def_points])
                        conn.commit()
                    pk += 1  # this gets set as the primary key
                check_name = playerName
    context = {'player_dict': player_dict}
    return render(request, 'nba-musicfiles_home.html', context)


# ===============================================================================================
#           SAVE SELECTED FAVORITES TO NEW DATABASE
# ===============================================================================================

def save_favorites(request, pk):
    player = get_object_or_404(PlayerDb, pk=pk)
    name = player.playerName
    defRebs = player.defRebs
    steals = player.steals
    blocks = player.blocks
    total = player.total

    # Connect to templates, delete record if the pk already exists
    conn = sqlite3.connect('db.sqlite3')
    with conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM NBAstats_FavoritesDB WHERE id = ?', [pk])

        cur.execute('INSERT INTO NBAstats_FavoritesDB VALUES (?,?,?,?,?,?)',
                    [pk, name, defRebs, steals, blocks, total])
        conn.commit()

    return redirect('favorites')
