from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .form import UserForm, PlayerForm, NewUserForm, TeamForm
from .models import Profile, FavPlayer
import requests
from bs4 import BeautifulSoup
import json


def IceHockey_logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("IceHockey_home")


def IceHockey_login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("IceHockey_home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "IceHockey/IceHockey_login.html", {"login_form": form})


def IceHockey_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            favorite_team = request.POST['favorite_team']
            favorite_player = request.POST['favorite_player']

            new_profile = Profile.Profile.create(

                first_name=first_name,
                last_name=last_name,
                favorite_team=favorite_team,
                favorite_player=favorite_player,
            )

            return redirect("IceHockey_home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "IceHockey/IceHockey_register.html", {"register_form": form})


def IceHockey_fav_add(request, pk):
    # keeps user data at hand for the final step in the saving process in the confirm add view.
    user = get_object_or_404(Profile, pk=pk)
    """
    When the user clicks the 'Add Fav' button from the api page, the form data is retrieved with 
    the code below, which is then passed along to the confirm add page in the same fashion.
    """
    if request.method == 'POST':
        name = request.POST['player_name']
        num = request.POST['player_num']
        pos = request.POST['player_pos']
        print(name)
        print(num)
        print(pos)
    return render(request, 'IceHockey/IceHockey_fav_add.html', {'name': name, 'num': num, 'pos': pos, 'user': user})


def IceHockey_show_favorites(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    player_list = FavPlayer.FavPlayer.filter(my_profile__exact=int(pk))
    return render(request, 'IceHockey/IceHockey_show_favorites.html', {'player_list': player_list, 'user': user})


def IceHockey_confirm_add(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    """
    We once again retrieve the relevant data from the form, passing it into variables
    that we can then input into the creation of a new favorite player object.  To combat the creation
    of duplicate entries, an if statement checks if the name being entered already exists 
    within the database.  
    """
    if request.method == 'POST':
        name = request.POST['player_name']
        num = request.POST['player_num']
        pos = request.POST['player_pos']

        if FavPlayer.FavPlayer.filter(name=name).exists():
            return render(request, 'IceHockey/IceHockey_confirm_add.html', {'user': user})
        else:
            new_player = user.favorite_player_list.create(
                my_profile=user,
                name=name,
                number=num,
                position=pos,
            )
            return render(request, 'IceHockey/IceHockey_confirm_add.html', {'user': user})


def IceHockey_home(request):
    news_titles = []
    news_links = []
    news_dates = []

    response = requests.get(
        'https://newsdata.io/api/1/news?apikey=pub_419404de6e248af4abb353fdc5168853dd51&q=ice%20hockey&country=ca,us&language=en')
    news = json.loads(response.text)
    results = news['results']
    for story in results:
        title = story['title']
        link = story['link']
        date = story['pubDate']

        news_links.append(link)
        news_titles.append(title)
        news_dates.append(date)

    zipped_list = zip(news_titles, news_links, news_dates)
    context = {'zipped_list': zipped_list}

    return render(request, 'IceHockey/IceHockey_home.html', context)


def IceHockey_newprofile(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('IceHockey_home')
    context = {'form': form}
    return render(request, 'IceHockey/IceHockey_newprofile.html', context)


def IceHockey_allprofiles(request, pk):
    profile_list = Profile.Profile.all()
    return render(request, 'IceHockey/IceHockey_allprofiles.html', {'profile_list': profile_list})


def IceHockey_myprofile(request, pk):
    profile_list = Profile.Profile.filter(id__exact=pk)
    return render(request, 'IceHockey/IceHockey_myprofile.html', {'profile_list': profile_list})


def IceHockey_details(request, pk):
    details = get_object_or_404(Profile, pk=pk)
    context = {'details': details}
    return render(request, 'IceHockey/IceHockey_details.html', context)


def IceHockey_error(request, pk):
    details = get_object_or_404(Profile, pk=pk)
    return render(request, 'IceHockey/IceHockey_error.html', details)


def IceHockey_scrapeddata(request, pk):
    player_years = []
    player_teams = []
    player_leagues = []
    player_goals = []
    player_assists = []
    test = []

    details = get_object_or_404(Profile, pk=pk)
    det_dict = {'details': details}

    # loads search page for elite prospects, a popular hockey database
    base_url = "https://www.eliteprospects.com/search/player?q="

    # grabs user's favorite player's name, modifies it for use in new url
    fav_name = str(details.favorite_player)
    split_name = fav_name.split()
    print(len(split_name))
    if len(split_name) < 2:
        return render(request, 'IceHockey/IceHockey_error.html', det_dict)
    new_name = split_name[0] + '+' + split_name[1]
    url = base_url + new_name
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    # searches all links in new url, finds link with player's first and last name
    for link in soup.find_all('a'):
        x = str(link.get('href'))
        if split_name[0].lower() and split_name[1].lower() in x:
            print(x)
            test = x.split("/")
            # assumes that first instance of match is correct, returns single result
            break

    if test:
        # creates player page url out of the id number (index 4), and the player name (index 5)
        player_id = test[4]
        player_name = test[5]
        soup2 = "https://www.eliteprospects.com/player/" + player_id + "/" + player_name
        new_result = requests.get(soup2)
        soup = BeautifulSoup(new_result.text, "html.parser")

        # finds all player's season years
        for seasons in soup.find_all('span', class_="season"):
            season = seasons.string
            player_years.append(season)

        # finds all player's team's names
        for teams in soup.find_all("td", class_="team"):
            for spans in teams.find_all('span'):
                for links in spans.find_all('a'):
                    team = links.string
                    player_teams.append(team)
                    break

        # finds all player's league names
        for leagues in soup.find_all("td", class_="league"):
            for links in leagues.find_all('a'):
                league = links.string
                player_leagues.append(league)

        # finds all player's goal totals
        for goals in soup.find_all("td", class_="regular g"):
            goal = goals.string
            player_goals.append(goal)

        # finds all player's assist totals
        for assists in soup.find_all("td", class_="regular a"):
            assist = assists.string
            player_assists.append(assist)

        # condenses all data arrays into single variable
        zipped_list = zip(player_years, player_teams, player_leagues, player_goals, player_assists)
        context = {'zipped_list': zipped_list, 'details': details}
        return render(request, 'IceHockey/IceHockey_scrapeddata.html', context)
    else:
        return render(request, 'IceHockey/IceHockey_error.html', det_dict)


def IceHockey_samplescrape(request):
    player_years = []
    player_teams = []
    player_leagues = []
    player_goals = []
    player_assists = []

    # loads search page for elite prospects, a popular hockey database
    base_url = "https://www.eliteprospects.com/search/player?q="

    # grabs user's favorite player's name, modifies it for use in new url
    new_name = 'Wayne+Gretzky'
    url = base_url + new_name
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    # searches all links in new url, finds link with player's first and last name
    for link in soup.find_all('a'):
        x = str(link.get('href'))
        if 'wayne' and 'gretzky' in x:
            print(x)
            test = x.split("/")
            # assumes that first instance of match is correct, returns single result
            break

    # creates player page url out of the id number (index 4), and the player name (index 5)
    player_id = test[4]
    player_name = test[5]
    soup2 = "https://www.eliteprospects.com/player/" + player_id + "/" + player_name
    new_result = requests.get(soup2)
    soup = BeautifulSoup(new_result.text, "html.parser")

    # finds all player's season years
    for seasons in soup.find_all('span', class_="season"):
        season = seasons.string
        player_years.append(season)

    # finds all player's team's names
    for teams in soup.find_all("td", class_="team"):
        for spans in teams.find_all('span'):
            for links in spans.find_all('a'):
                team = links.string
                player_teams.append(team)
                break

    # finds all player's league names
    for leagues in soup.find_all("td", class_="league"):
        for links in leagues.find_all('a'):
            league = links.string
            player_leagues.append(league)

    # finds all player's goal totals
    for goals in soup.find_all("td", class_="regular g"):
        goal = goals.string
        player_goals.append(goal)

    # finds all player's assist totals
    for assists in soup.find_all("td", class_="regular a"):
        assist = assists.string
        player_assists.append(assist)

    # condenses all data arrays into single variable
    zipped_list = zip(player_years, player_teams, player_leagues, player_goals, player_assists)
    context = {'zipped_list': zipped_list}
    return render(request, 'IceHockey/IceHockey_samplescrape.html', context)


def IceHockey_edit(request, pk):
    item = get_object_or_404(Profile, pk=pk)
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('IceHockey_myprofile', pk)
    context = {'form': form}
    return render(request, 'IceHockey/IceHockey_edit.html', context)


def IceHockey_delete(request, pk):
    item = get_object_or_404(Profile, pk=pk)
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('IceHockey_myprofile')
    return render(request, 'IceHockey/IceHockey_delete.html', {'item': item, 'form': form})


def IceHockey_api_choice(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    form = TeamForm()

    if request.method == 'POST':
        team_choice = request.POST['team_choice']
        roster = []
        player_list = []
        number_list = []
        position_list = []
        position_code = []

        # finds list of all teams from api
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
        teams_info = json.loads(response.text)
        team_list = teams_info['teams']
        for team in team_list:
            teamname = team['name']
            teamid = team['id']

            # matches user's favorite team with response
            if teamname == team_choice:
                urlid = teamid
                urlname = teamname

        # updates url with user's team id to find roster info
        roster_response = requests.get('https://statsapi.web.nhl.com/api/v1/teams' + '/' + str(urlid) + '/roster')
        roster_info = json.loads(roster_response.text)
        roster_list = roster_info['roster']

        # retrieves player's name, jersey number, and position code.
        for player in roster_list:
            item = player['person']
            player_list.append(item)
            playername = item['fullName']
            roster.append(playername)

            item2 = player['jerseyNumber']
            number_list.append(item2)

            item3 = player['position']
            position_list.append(item3)
            item4 = item3['code']
            position_code.append(item4)

        print(roster)
        print(position_code)
        print(number_list)

        zipped_list = zip(roster, position_code, number_list)
        context = {'zipped_list': zipped_list, 'urlname': urlname, 'urlid': urlid, 'user': user, 'form': form}

        return render(request, 'IceHockey/IceHockey_api_choice.html', context)


def IceHockey_api_page(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    form = TeamForm()
    roster = []
    player_list = []
    number_list = []
    position_list = []
    position_code = []

    # finds list of all teams from api
    response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
    teams_info = json.loads(response.text)
    team_list = teams_info['teams']
    for team in team_list:
        teamname = team['name']
        teamid = team['id']

        # matches user's favorite team with response
        if teamname == user.favorite_team:
            urlid = teamid
            urlname = teamname

    # updates url with user's team id to find roster info
    roster_response = requests.get('https://statsapi.web.nhl.com/api/v1/teams' + '/' + str(urlid) + '/roster')
    roster_info = json.loads(roster_response.text)
    roster_list = roster_info['roster']

    # retrieves player's name, jersey number, and position code.
    for player in roster_list:
        item = player['person']
        player_list.append(item)
        playername = item['fullName']
        roster.append(playername)

        item2 = player['jerseyNumber']
        number_list.append(item2)

        item3 = player['position']
        position_list.append(item3)
        item4 = item3['code']
        position_code.append(item4)

    print(roster)
    print(position_code)
    print(number_list)

    zipped_list = zip(roster, position_code, number_list)
    context = {'zipped_list': zipped_list, 'urlname': urlname, 'urlid': urlid, 'user': user, 'form': form}
    return render(request, 'IceHockey/IceHockey_api_page.html', context)


def IceHockey_sampleapi(request):
    roster = []
    player_list = []
    number_list = []
    position_list = []
    position_code = []

    # finds list of all teams from api
    response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
    teams_info = json.loads(response.text)
    team_list = teams_info['teams']
    for team in team_list:
        teamname = team['name']
        teamid = team['id']

        # matches user's favorite team with response
        if teamname == 'Vancouver Canucks':
            urlid = teamid
            urlname = teamname

    # updates url with user's team id to find roster info
    roster_response = requests.get('https://statsapi.web.nhl.com/api/v1/teams' + '/' + str(urlid) + '/roster')
    roster_info = json.loads(roster_response.text)
    roster_list = roster_info['roster']

    # retrieves player's name, jersey number, and position code.
    for player in roster_list:
        item = player['person']
        player_list.append(item)
        playername = item['fullName']
        roster.append(playername)

        item2 = player['jerseyNumber']
        number_list.append(item2)

        item3 = player['position']
        position_list.append(item3)
        item4 = item3['code']
        position_code.append(item4)

    print(roster)
    print(position_code)
    print(number_list)

    zipped_list = zip(roster, position_code, number_list)
    context = {'zipped_list': zipped_list, 'urlname': urlname, 'urlid': urlid}

    return render(request, 'IceHockey/IceHockey_sampleapi.html', context)
