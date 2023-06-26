from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import GamesForm, PublishersForm
from .models import Games, FavoriteGame
import requests
from bs4 import BeautifulSoup
import json


def homepage(request):
    return render(request, 'GameStats/gamestats_home.html')

def add_game(request):
    form = GamesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'GameStats/gamestats_home.html')
    context = {'form': form}
    return render(request, 'GameStats/gamestats_create.html', context)


def view_games(request):
    query = request.GET
    context = {}
    # for some reason .all() doesn't work here, instead we will do filter and not include anything *yet*
    # get all and return with no filtering
    game_list = Games.Game.filter()
    if query and request.method == 'GET':
        # filter if we are searching
        if query.get('search_res', None):
            game_list = Games.Game.filter(rating=query.get('search_res', None))
        elif query.get('release_year', None):
            game_list = Games.Game.filter(release_year=query.get('release_year', None))
        elif query.get('genre', None):
            game_list = Games.Game.filter(genre=query.get('genre', None))
        elif query.get('name', None):
            game_list = Games.Game.filter(name=query.get('name', None))
        # game_list = Games.Game.filter(rating=query.get('search_res', None), release_year=query.get('release_year', None),
        #                               genre=query.get('genre', None), name=query.get('name', None))

    game = request.GET.get('page', 1)
    paginator = Paginator(game_list, 10)

    try:
        game_list = paginator.page(game)
    except PageNotAnInteger:
        game_list = paginator.page(1)
    except EmptyPage:
        game_list = paginator.page(paginator.num_pages)

    context = { 'game_list': game_list }
    return render(request, 'GameStats/gamestats_all.html', context)

def game_details(request, pk):
    details = get_object_or_404(Games, pk=pk)
    context = {'details': details}
    return render(request, 'GameStats/gamestats_details.html', context)

def game_edit(request, pk):
    details = get_object_or_404(Games, pk=pk)
    form = GamesForm(data=request.POST or None, instance=details)
    if request.method == 'POST':
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('gamestats_viewall')
        else:
            print('valid')
    context = {'form': form}
    return render(request, 'GameStats/gamestats_edit.html', context)

def game_delete(request, pk):
    details = get_object_or_404(Games, pk=pk)
    form = GamesForm(data=request.POST or None, instance=details)
    if request.method == 'POST':
        details.delete()
        return redirect('gamestats_viewall')
    context = { 'details': details, 'form': form }
    return render(request, 'GameStats/gamestats_delete.html', context)

def favorite_delete(pk):
    FavoriteGame.Favorites.filter(id=pk).delete()

def top_games(request):
    review_dict = scrape_site()

    name = review_dict['name']
    date = review_dict['date']
    rating = review_dict['rating']
    gameId = review_dict['id']
    test = zip(name, date, rating, gameId)
    context = {'data': test, 'passed': False}
    return render(request, 'GameStats/gamestats_topgames.html', context)

def top_game_one(request, id):
    review_dict = scrape_site()
    favorited = check_fav_duplicate(review_dict['name'][id])
    pk = get_fav_id(review_dict['name'][id])
    if request.method == 'POST':
        if favorited:
            favorite_delete(pk)
        else:
            try_add_favorite(review_dict['name'][id], review_dict['rating'][id], review_dict['date'][id])
        favorited = not favorited
    context = {'name': review_dict['name'][id], 'date': review_dict['date'][id], 'rating': review_dict['rating'][id],
               'image': review_dict['image'][id], 'summary': review_dict['summary'][id], 'status': favorited, 'id': pk }
    return render(request, 'GameStats/gamestats_view_one.html', context)

def scrape_site():
    url = 'https://www.metacritic.com/game'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent)

    soup = BeautifulSoup(response.text, 'html.parser')
    review_dict = {'name': [], 'date': [], 'rating': [], 'image': [], 'summary': [], 'id': []}

    tempID = 0
    for review in soup.find_all('tr'):
        if review.find("div", class_='clamp-score-wrap'):
            # had to strip everything down because websites add lots of spaces.
            # title
            review_dict['name'].append(review.find("h3").text.strip())
            # score
            review_dict['rating'].append(review.find("div", class_='clamp-score-wrap').text.strip())
            # image URL
            review_dict['image'].append(review.find("img")["src"])
            # summary
            review_dict['summary'].append(review.find(class_="summary").text.strip())

            # release date
            a = review.find_all(class_="clamp-details")
            for element in a:
                try:
                    # print(element.find("span").text.strip())
                    # in the event we come up with something other than a normal string, .text.strip() won't work
                    # thus cleaning invalid inputs, and we just don't add to the dict if they are invalid
                    review_dict['date'].append(element.find("span").text.strip())
                except AttributeError:
                    pass
            review_dict['id'].append(tempID)
            tempID += 1
    return review_dict

def api_game_view(request):
    """
    Tried a few different apis for this, they are awful
    This was the most consistent that had decent documentation
    I'm still relatively limited but I can make do with it
    My initial goal was to search by genre, or do a release date search
    but that doesn't work, instead we're just gonna do an explore page
    """
    query = request.GET
    # for some reason .all() doesn't work here, instead we will do filter and not include anything *yet*
    # get all and return with no filtering
    query_options = ""
    if query and request.method == 'GET':
        if query.get('name', None):
            query_options = '&query={}'.format(query.get('name', None))

    filtered_responses = api_query(query_options)

    # for item in filtered_responses['genres']:
    #     item = str(item).strip("[]")
    # print(filtered_responses['name'])
    for i in range(len(filtered_responses['genres'])):
        filtered_responses['genres'][i] = str(filtered_responses['genres'][i]).strip("[]").replace("'", "")

    dataList = zip(filtered_responses['name'], filtered_responses['genres'], filtered_responses['release_date'])
    context = {'data': dataList}

    return render(request, 'GameStats/gamestats_explore.html', context)

def api_query(options=None):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    req_url = "https://www.giantbomb.com/api/games/?api_key=8c2a3059218223501315304c270747790b292c62"
    if options:
        req_url = "http://www.giantbomb.com/api/search?api_key=8c2a3059218223501315304c270747790b292c62"
    # limit 5 for testing purposes.
    # set to 10 for main integration
    filters = "&limit=10&format=json"
    filters += options
    # print(req_url + filters)
    req = requests.get(req_url + filters, headers=user_agent)
    filtered_responses = {'name': [], 'genres': [], 'release_date': []}
    # print(test)
    try:
        # load json object
        # .json() wasn't working, so load it in from text
        response_obj = json.loads(req.text)
        # generally works but doesn't always have an actual release date
        # print(response_obj['results'][0]['original_release_date'])
        # print(response_obj['results'][0]['name'])

        # the amount of data and the way they sort it is ridiculous
        for i in range(len(response_obj['results'])):
            # print(response_obj['results'][i]['name'])
            # each specific piece of data has its potential for an expection
            try:
                # if this tosses an exception we don't want to add any other data
                # otherwise it will misalign names with incorrect data
                # so skip it and the rest of this loop, on to the next iteration
                filtered_responses['name'].append(response_obj['results'][i]['name'])
            except:
                continue
            try:
                # if this one errors, none were found and we just need to list that
                # limitation of the api data.
                filtered_responses['genres'].append(get_api_genres(i, response_obj))
            except:
                filtered_responses['genres'].append("None found")
            try:
                # if this one errors, none were found and we just need to list that
                # limitation of the api data.
                filtered_responses['release_date'].append(response_obj['results'][i]['original_release_date'])
            except:
                # print(response_obj['results'][i]['expected_release_year'])
                filtered_responses['release_date'].append(response_obj['results'][i]['expected_release_year'])
    except Exception as e:
        # not a necessary print, sometimes there is a json error though for bad data
        print(e)

    return filtered_responses

def get_api_genres(id, obj):
    """
    I don't like having to make this many api requests at once, but the api doesn't give me a choice
    I can't pull multiple items and get their genre, I have to get all the items and use their id to do a specific
    search to get their genre. 1 request turns into a request for each game on top of the initial request.
    """
    # still important
    user_agent = {'User-agent': 'Mozilla/5.0'}
    # region Genres
    get_genre_url_settings = "&format=json"
    get_genre_url = "https://www.giantbomb.com/api/game/{}/?api_key=8c2a3059218223501315304c270747790b292c62".format(
        obj['results'][id]['guid'])
    get_genre = requests.get(get_genre_url + get_genre_url_settings, headers=user_agent)
    genre_obj = json.loads(get_genre.text)
    tempGenresList = []
    # create a list of genre names to add to the dictionary
    for i in range(len(genre_obj['results']['genres'])):
        tempGenresList.append(genre_obj['results']['genres'][i]['name'])
        # print(genre_obj['results']['genres'][i]['name'])
    return tempGenresList

    # endregion

def add_favorite_page(request):
    # we get name, rating, release date
    data = scrape_site()
    context = { 'names': data['name'] }
    query = request.GET
    if query and request.method == 'GET':
        if query.get('value', None):
            index = 0
            for i in range(len(data['name'])):
                if data['name'][i] == query.get('value', None):
                    index = i
                    break

            fav = try_add_favorite(data['name'][index], data['rating'][index], data['date'][index])
            if not fav:
                return redirect('gamestats_view_favorites')
            else:
                context['alert'] = True
    return render(request, 'GameStats/gamestats_add_favorite.html', context)

def try_add_favorite(name, rating, release):
    duplicate = check_fav_duplicate(name)

    if not duplicate:
        added_game = FavoriteGame.Favorites.create(name=name, release_date=release, rating=rating)
        added_game.save()

    return duplicate

def check_fav_duplicate(name):
    favorites_list = FavoriteGame.Favorites.filter()
    duplicate = False
    for item in favorites_list:
        if name == item.name:
            duplicate = True
            break
    return duplicate

def get_fav_id(name):
    # although name TECHNICALLY doesn't have to be unique
    # it also does since 2 of the same name won't be allowed in the same favorites list
    favorites_list = FavoriteGame.Favorites.all()
    for item in favorites_list:
        if item.name == name:
            return item.pk

def view_favorites(request):
    favorites_list = FavoriteGame.Favorites.all()

    if request.method == 'POST':
        for item in favorites_list:
            if item.name in request.POST:
                favorite_delete(get_fav_id(item.name))

    favorites_list = FavoriteGame.Favorites.all()
    context = { 'favorites': favorites_list }
    return render(request, 'GameStats/gamestats_view_favorites.html', context)

