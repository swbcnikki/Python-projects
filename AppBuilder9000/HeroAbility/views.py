from django.shortcuts import render, redirect, get_object_or_404
from .models import Heroes
from .forms import HeroForm
import requests
import json


# calls the heroability home page when requested
def heroability_home(request):
    return render(request, 'HeroAbility/heroability_home.html')


# call template and accept the form inputs for adding to the db
def heroability_new_hero(request):
    form = HeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('heroability_display_all')
    else:
        print(form.errors)
        form = HeroForm()
    content = {
        'form': form,
    }
    return render(request, 'HeroAbility/heroability_new_hero.html', content)


# call all records and the display template
def heroability_display_all(request):
    heroes = Heroes.heroes.all()
    content = {
        'heroes': heroes,
    }
    return render(request, 'HeroAbility/heroability_display_all.html', content)


# call the details template
def heroability_details(request, pk):
    pk = int(pk)
    hero = get_object_or_404(Heroes, pk=pk)
    form = HeroForm(data=request.POST or None, instance=hero)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('heroability_display_all')
        else:
            print(form.errors)
    else:
        content = {
            'form': form,
            'hero': hero,
        }
        return render(request, 'HeroAbility/heroability_details.html', content)


# call template to confirm we are deleting from the db
def heroability_delete_hero(request, pk):
    pk = int(pk)
    hero = get_object_or_404(Heroes, pk=pk)
    if request.method == 'POST':
        hero.delete()
        return redirect('heroability_display_all')
    content = {
        "hero": hero,
    }
    return render(request, "HeroAbility/heroability_confirm_delete.html", content)


# function used to confirm the delete action
def heroability_confirm_delete(request):
    if request.method == 'POST':
        form = HeroForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('heroability_display_all')
    else:
        return redirect('heroability_display_all')


# Using an API to call more heroes that could potentially be added
def heroability_fetch_heroes():
    random_hero_alias = {}
    random_hero_name = {}
    url = "https://superhero-search.p.rapidapi.com/api/heroes"

    headers = {
        "X-RapidAPI-Host": "superhero-search.p.rapidapi.com",
        "X-RapidAPI-Key": "2345c7543fmshca4cdeb5e63abb6p10eacbjsna1f873331a65"
    }

    response = requests.request("GET", url, headers=headers)
    new_heroes = json.loads(response.text)
    for new_hero in new_heroes: # loop through the items provided in the API response ad add them to 2 sperate lists
        random_hero_alias[new_hero['name']] = new_hero['name']
        random_hero_name[new_hero['biography']['fullName']] = new_hero['biography']['fullName']
    random_heroes = zip( # create a zip to consolidate the data that can be displayed more easily
        random_hero_alias,
        random_hero_name,
    )
    return random_heroes


# call the template to display the api call
def heroability_random_heroes(request):
    random_heroes = heroability_fetch_heroes()
    content = {
        'random_heroes': random_heroes
    }
    return render(request, "HeroAbility/heroability_random_heroes.html", content)
