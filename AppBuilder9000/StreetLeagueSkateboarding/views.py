# Imports;
from django.shortcuts import render, redirect, get_object_or_404
from .models import Skater, WeatherMoment
from .forms import EntryForm, WeatherMomentForm
import requests
import json
from bs4 import BeautifulSoup
import datetime

# Functions;
def SLS_home(request):
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_home.html')

def SLS_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("StreetLeagueSkateboarding_view")
    content = {'form': form}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_create.html', content)

def SLS_view(request):
    entry = Skater.Entry.all()
    content = {'entry': entry}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_view.html', content)

def SLS_details(request, pk):
    entry = get_object_or_404(Skater, pk=pk)
    content = {'entry': entry}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_details.html', content)

def SLS_update(request, pk):
    entry = get_object_or_404(Skater, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('StreetLeagueSkateboarding_view')
    content = {'form': form, 'entry': entry}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_update.html', content)

def SLS_delete(request, pk):
    entry = get_object_or_404(Skater, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('StreetLeagueSkateboarding_view')
    content = {'entry': entry}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_delete.html', content)

def SLS_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "findlay", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "81272c5418msh25156274a12ae48p1c7bdajsn0ce401ff9166"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_api.html', content)

def SLS_save_api(request, m=1000):
    if m != 1000:
        moment = WeatherMoment(
            temperature=m
        )
        moment.save()
    moment = WeatherMoment.WeatherMoments.all()
    content = {"moment": moment}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_save_api.html', content)

def SLS_bs(request):
    page = requests.get("https://www.skatedeluxe.com/blog/en/wiki/skateboarding/history-of-skateboarding/")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[0].get_text()
    content = {"info": info}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_bs.html', content)