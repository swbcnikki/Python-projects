from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayersForm, TeamsForm
from .models import Players, Teams
import requests
import json
from bs4 import BeautifulSoup


def home(request):
    return render(request, 'BasketballStats/BasketballStats_home.html')


"""
=========================================================================================================
    CRUD SECTION - MODEL: PLAYERS 
=========================================================================================================
"""


def create_player(request):
    form = PlayersForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('basketball_stats_players')
    context = {'form': form}
    return render(request, 'BasketballStats/BasketballStats_create.html', context)


# Display all Players created
def player_stats(request):
    player_list = Players.Player.all()
    context = {'player_list': player_list}
    return render(request, 'BasketballStats/BasketballStats_players.html', context)


def player_details(request, pk):
    details = get_object_or_404(Players, pk=pk)
    context = {'details': details}
    return render(request, 'BasketballStats/BasketballStats_details.html', context)


def player_edit(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('basketball_stats_players')
    context = {'form': form}
    return render(request, 'BasketballStats/BasketballStats_edit.html', context)


def player_delete(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('basketball_stats_players')
    return render(request, 'BasketballStats/BasketballStats_delete.html', {'item': item, 'form': form})


"""
=========================================================================================================
    CRUD SECTION - MODEL: TEAMS
=========================================================================================================
"""


def view_favorites(request):
    team_list = Teams.Team.all()
    context = {'team_list': team_list}
    return render(request, 'BasketballStats/BasketballStats_favorite_teams.html', context)


def team_delete(request, pk):
    item = get_object_or_404(Teams, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('basketball_stats_favorites')
    return render(request, 'BasketballStats/BasketballStats_delete_favorites.html', {'item': item, 'form': form})


"""
=========================================================================================================
    FAVORITE TEAM DETAILS SECTION
=========================================================================================================
"""


# This function creates a dictionary for each team name and each team's abbreviated name
# The abbreviated name will be used in the favorite_team_details function
def abbreviate_name():
    team_list = Teams.Team.all()
    abbrev = {}
    for team in team_list:
        if team.team_name == 'Atlanta Hawks':
            abbrev[team.team_name] = 'ATL'
        elif team.team_name == 'Boston Celtics':
            abbrev[team.team_name] = 'BOS'
        elif team.team_name == 'Brooklyn Nets':
            abbrev[team.team_name] = 'BRK'
        elif team.team_name == 'Charlotte Hornets':
            abbrev[team.team_name] = 'CHO'
        elif team.team_name == 'Chicago Bulls':
            abbrev[team.team_name] = 'CHI'
        elif team.team_name == 'Cleveland Cavaliers':
            abbrev[team.team_name] = 'CLE'
        elif team.team_name == 'Dallas Mavericks':
            abbrev[team.team_name] = 'DAL'
        elif team.team_name == 'Denver Nuggets':
            abbrev[team.team_name] = 'DEN'
        elif team.team_name == 'Detroit Pistons':
            abbrev[team.team_name] = 'DET'
        elif team.team_name == 'Golden State Warriors':
            abbrev[team.team_name] = 'GSW'
        elif team.team_name == 'Houston Rockets':
            abbrev[team.team_name] = 'HOU'
        elif team.team_name == 'Indiana Pacers':
            abbrev[team.team_name] = 'IND'
        elif team.team_name == 'Los Angeles Clippers':
            abbrev[team.team_name] = 'LAC'
        elif team.team_name == 'Los Angeles Lakers':
            abbrev[team.team_name] = 'LAL'
        elif team.team_name == 'Memphis Grizzlies':
            abbrev[team.team_name] = 'MEM'
        elif team.team_name == 'Miami Heat':
            abbrev[team.team_name] = 'MIA'
        elif team.team_name == 'Milwaukee Bucks':
            abbrev[team.team_name] = 'MIL'
        elif team.team_name == 'Minnesota Timberwolves':
            abbrev[team.team_name] = 'MIN'
        elif team.team_name == 'New Orleans Pelicans':
            abbrev[team.team_name] = 'NOP'
        elif team.team_name == 'New York Knicks':
            abbrev[team.team_name] = 'NYK'
        elif team.team_name == 'Oklahoma City Thunder':
            abbrev[team.team_name] = 'OKC'
        elif team.team_name == 'Orlando Magic':
            abbrev[team.team_name] = 'ORL'
        elif team.team_name == 'Philadelphia 76ers':
            abbrev[team.team_name] = 'PHI'
        elif team.team_name == 'Phoenix Suns':
            abbrev[team.team_name] = 'PHO'
        elif team.team_name == 'Portland Trail Blazers':
            abbrev[team.team_name] = 'POR'
        elif team.team_name == 'Sacramento Kings':
            abbrev[team.team_name] = 'SAC'
        elif team.team_name == 'San Antonio Spurs':
            abbrev[team.team_name] = 'SAS'
        elif team.team_name == 'Toronto Raptors':
            abbrev[team.team_name] = 'TOR'
        elif team.team_name == 'Utah Jazz':
            abbrev[team.team_name] = 'UTA'
        elif team.team_name == 'Washington Wizards':
            abbrev[team.team_name] = 'WAS'
    return abbrev


# This function iterates through all of the favorite teams to assign the abbreviated names to them
# It then checks if the team selected for the details page is equal to a name in the favorite team list
# Once an equal name has been found it passes the abbreviated name of the selected favorite team into the url
# for BeautifulSoup. Then it appends an empty list so that list can be passed to the favorite team details template
def favorite_team_details(request, pk):
    details = get_object_or_404(Teams, pk=pk)
    team_list = Teams.Team.all()
    info = []
    for team in team_list:
        name = team.team_name
        abbrev = abbreviate_name()
        abr_name = abbrev[team.team_name]
        if details.team_name == name:
            page = requests.get("https://www.basketball-reference.com/teams/" + str(abr_name) + "/2022.html")
            soup = BeautifulSoup(page.content, 'html.parser')
            meta = soup.find('div', id='meta')
            ptags = meta.find_all('p')[2:]
            for i in ptags:
                text = i.text.strip()
                info.append(text)
    return render(request, 'BasketballStats/BasketballStats_favorite_details.html', {'details': details,
                                                                                     'info': info})


"""
=========================================================================================================
    API SECTION 
=========================================================================================================
"""


# This function matches team names with the team IDs from the API. It returns a key-value pair dictionary
# with the ID being the key, and the value being the team's full name
def fetch_team_name():
    full_name = {}
    url = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"
    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "93c897feddmshe43ca8b1cec9f29p1e574bjsn0ad1ca76158a"
    }
    response = requests.request("GET", url, headers=headers)
    team_names = json.loads(response.text)
    for teams in team_names['api']['teams']:
        if teams['nbaFranchise'] == '1':
            full_name[teams['teamId']] = teams['fullName']
    return full_name


# This function gets all NBA teams, then puts them into lists representing each conference in the league
# Once in the list has all the teams they are sorted by their rank in the conference. The user selects
# which season to view the standings for
def standings_page(request):
    west_team = []
    east_team = []
    season = ' '
    if 'season' in request.POST:
        full_name_dict = fetch_team_name()
        season = request.POST['season']
        url = 'https://api-nba-v1.p.rapidapi.com/standings/standard/' + season
        headers = {
             'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
             'x-rapidapi-key': "93c897feddmshe43ca8b1cec9f29p1e574bjsn0ad1ca76158a"
        }
        response = requests.request("GET", url, headers=headers)
        team_standings = json.loads(response.text)
        for team in team_standings['api']['standings']:
            team_name = full_name_dict[team['teamId']]
            ranking = team['conference']['rank']
            team_result = (ranking, team_name)
            if team['conference']['name'] == 'west':
                west_team.append(team_result)
            else:
                east_team.append(team_result)
            west_team.sort(key=lambda a: int(a[0]))
            east_team.sort(key=lambda a: int(a[0]))
    context = {'west_team': west_team, 'east_team': east_team, 'season': season}
    return render(request, 'BasketballStats/BasketballStats_team_standings.html', context)


# This function puts each team in a list that represents their division within the league. It also
# grabs the logo for each team. The divisions are then zipped into eastern and western conferences
def conference_division(request):
    atlantic = []
    central = []
    southeast = []
    northwest = []
    pacific = []
    southwest = []
    utah_teams = []
    atlantic_logos = []
    central_logos = []
    southeast_logos = []
    northwest_logos = []
    pacific_logos = []
    southwest_logos = []
    url = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"

    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "93c897feddmshe43ca8b1cec9f29p1e574bjsn0ad1ca76158a"
    }

    response = requests.request("GET", url, headers=headers)
    teams_info = json.loads(response.text)
    team_list = teams_info['api']['teams']
    for teams in team_list:
        name = teams['fullName']
        logo = teams['logo']
        division = teams['leagues']['standard']['divName']

        if division == 'Atlantic':
            atlantic.append(name)
            atlantic_logos.append(logo)

        elif division == 'Central':
            central.append(name)
            central_logos.append(logo)

        elif division == 'Southeast':
            southeast.append(name)
            southeast_logos.append(logo)

        elif division == 'Northwest':
            if name == 'Utah Blue':
                utah_teams.append(name)
            elif name == 'Utah White':
                utah_teams.append(name)
            else:
                northwest.append(name)
                northwest_logos.append(logo)

        elif division == 'Pacific':
            pacific.append(name)
            pacific_logos.append(logo)

        elif division == 'Southwest':
            southwest.append(name)
            southwest_logos.append(logo)

    eastern_conference = zip(atlantic, central, southeast)
    western_conference = zip(northwest, pacific, southwest)
    context = {
        'eastern_conference': eastern_conference, 'western_conference': western_conference,
        'atlantic': atlantic, 'central': central, 'southeast': southeast,
        'northwest': northwest, 'pacific': pacific, 'southwest': southwest,
        'atlantic_logos': atlantic_logos, 'central_logos': central_logos, 'southeast_logos': southeast_logos,
        'northwest_logos': northwest_logos, 'pacific_logos': pacific_logos, 'southwest_logos': southwest_logos
    }
    return render(request, 'BasketballStats/BasketballStats_bdl_api.html', context)


# This function allows users to select their favorite NBA team from a dropdown menu. When the user
# clicks on submit the selected team is then saved to the database a favorite team
def save_favorites(request):
    team_names = []
    url = "https://www.balldontlie.io/api/v1/teams"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    team_list = data['data']
    for x in team_list:
        team_name = x['full_name']
        team_names.append(team_name)
    if request.method == 'POST':
        value = request.POST['value']
        print(value)
        for i in team_list:
            names = i['full_name']
            if value == names:
                new_team = Teams.Team.create(team_name=i['full_name'],
                                             conference=i['conference'],
                                             division=i['division']
                                             )
                new_team.save()
        return redirect('basketball_stats_favorites')
    else:
        return render(request, 'BasketballStats/BasketballStats_save_api.html', {'team_names': team_names})


"""
=========================================================================================================
    BEAUTIFULSOUP SECTION 
=========================================================================================================
"""


# This grabs a table of NBA Champions
def history_scraping(request):
    champion_list = []
    page = requests.get("https://www.dunkest.com/en/nba/news/58063/nba-champions-winners-1947-2021")
    soup = BeautifulSoup(page.content, 'html.parser')
    previous_champions = soup.find('section', class_='post__content text-article')
    champions = previous_champions.find_all('tr')[1:]
    for tr in champions:
        td = tr.find_all('td')
        row = [i.text for i in td]
        cells = row
        champion_list.append(cells)
    context = {'champion_list': champion_list}
    return render(request, 'BasketballStats/BasketballStats_history.html', context)


# Gets Portland Trail Blazer Roster from basketball-reference.com
def web_scraping(request):
    player_numbers = []
    roster = []
    position = []
    height = []
    weight = []
    birthday = []
    years_experience = []
    college = []
    page = requests.get("https://www.basketball-reference.com/teams/POR/2022.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', id='roster')
    tbody = table.find('tbody')
    th = tbody.find_all('th')

    # Get Player numbers
    for i in th:
        numbers = i.text
        player_numbers.append(numbers)

    # Get all tds to append lists
    tr = tbody.find_all('tr')
    for tds in tr:
        td_list = tds.find_all('td')

        # Get Player names
        name_list = td_list[0]
        names = name_list.text
        roster.append(names)

        # Get Player positions
        pos_list = td_list[1]
        pos = pos_list.text
        position.append(pos)

        # Get Player heights
        height_list = td_list[2]
        heights = height_list.text
        height.append(heights)

        # Get Player weights
        weight_list = td_list[3]
        weights = weight_list.text
        weight.append(weights)

        # Get Player birthdays
        bday_list = td_list[4]
        bdays = bday_list.text
        birthday.append(bdays)

        # Get Player years experience
        experience_list = td_list[6]
        exp = experience_list.text
        years_experience.append(exp)

        # Get Player colleges
        college_list = td_list[7]
        colleges = college_list.text
        college.append(colleges)

    # Zip lists together to easily display all data
    zipped_list = zip(player_numbers, roster, position, height, weight, birthday, years_experience, college)
    context = {
        'zipped_list': zipped_list
    }
    return render(request, 'BasketballStats/BasketballStats_web_scraping.html', context)
