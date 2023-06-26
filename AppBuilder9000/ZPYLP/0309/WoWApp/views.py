from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateCharacter
from .models import Character
from django.core.paginator import Paginator
from bs4 import BeautifulSoup
import requests
import re
# Create your views here.

def home(request):
    #using the django render function to show the WoWApp_home.html file
    return render(request, 'WoWApp/WoWApp_home.html')

def character_create_view(request):
    form = CreateCharacter(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('WoWApp_home')
    return render(request, "WoWApp/WoWApp_character_create.html", {'form': form})

def character_list_view(request):
    characters_list = Character.object.all()
    paginator = Paginator(characters_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        characters = paginator.page(page)
    except(EmptyPage, InvalidPage):
        characters = paginator.page(paginator.num_pages)
    return render(request, 'WoWApp/WoWApp_character_list.html', {'characters': characters})

def character_delete_view(request, pk):
    characters = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        characters.delete()
        return redirect('WoWAppCharacterList')
    return render(request, 'WoWApp/WoWApp_character_delete.html', {'characters': characters})

def generate_character(request, pk):
    characters = get_object_or_404(Character, pk=pk)
    return render(request, 'WoWApp/WoWApp_generate_character.html', {'characters': characters})

def character_detail_view(request, pk):
    characters = get_object_or_404(Character, pk=pk)
    return render(request, 'WoWApp/WoWApp_character_detail.html', {'characters': characters})

def character_edit_view(request, pk):
    characters = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CreateCharacter(request.POST, instance=characters)
        if form.is_valid():
            characters.save()
            return redirect('WoWAppCharacterDetail', pk=characters.pk)
    else:
        form = CreateCharacter(instance=characters)
    return render(request, 'WoWApp/WoWApp_character_edit.html', {'form': form})

def game_news_view(request):
    page = requests.get('https://wow.gamepedia.com/Wowpedia/News')
    soup = BeautifulSoup(page.content, 'html.parser')
    game_news_section = soup.find(class_='mw-parser-output')
    game_news = game_news_section.find('dl')
    titles = game_news.find_all('dt')
    descriptions = game_news.find_all('dd')
    game_list = []

    for x in range(0, len(titles) - 1):
        game = {
            "title": titles[x].get_text(),
            "description": descriptions[x].get_text(),
        }
        # childtag = titles[x].find('a')
        # if not childtag:
        #     game.update({"title": titles[x].get_text("dt")})
        #
        # childtag = descriptions[x].find('a')
        # if not childtag:
        #     game.update({"description": descriptions[x].get_text("dd")})

        game_list.append(game)

    print(game_list)

    return render(request, 'WoWApp/WoWApp_news_game.html', {'game_list': game_list})
