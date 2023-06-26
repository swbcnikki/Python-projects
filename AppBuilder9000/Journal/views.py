from django.shortcuts import render, redirect,  get_object_or_404
from .models import Entry, WeatherMoment
from .forms import EntryForm, WeatherMomentForm
import requests
import json
from bs4 import BeautifulSoup
import datetime


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def journal_home(request):
    return render(request, 'Journal/journal_home.html')


# Story #2: Create your model ------------------------------------------------------------------------------------------

def journal_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'Journal/journal_create.html', content)


# Story #3: Display all items from database ----------------------------------------------------------------------------

def journal_read(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'Journal/journal_read.html', content)


# Story #4: Details page -----------------------------------------------------------------------------------------------

def journal_details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    content = {'entry': entry}
    return render(request, 'Journal/journal_details.html', content)


# Story #5: Edit and Delete Functions ----------------------------------------------------------------------------------

def journal_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    return render(request, 'Journal/journal_update.html', content)


def journal_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../read')
    content = {'entry': entry}
    return render(request, 'Journal/journal_delete.html', content)


# Story #6-(API Pt 1): Connect to API ----------------------------------------------------------------------------------
# Story #7-(API Pt 2): Parse through JSON

def journal_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "portland", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "aa3d3af1d8mshe07b323c70b5c20p174de6jsn68e2b0bf2a3b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'Journal/journal_api.html', content)


# Story #6-(BS Pt 1): Setup Beautiful Soup -----------------------------------------------------------------------------
# Story #7-(BS Pt 2): Parse through html

def journal_bs(request):
    page = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[0].get_text()
    content = {"info": info}
    return render(request, 'Journal/journal_bs.html', content)


# Story #9: Save API or scraped results --------------------------------------------------------------------------------

def journal_save_api(request, m=1000):
    if m != 1000:
        moment = WeatherMoment(
            temperature=m
        )
        moment.save()
    moment = WeatherMoment.WeatherMoments.all()
    content = {"moment": moment}
    return render(request, 'Journal/journal_save_api.html', content)
