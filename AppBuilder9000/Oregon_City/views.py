from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from .forms import ActivityForm
import requests
import json


# Story #1: Build the basic app ---


def oregon_home(request):
    return render(request, 'Oregon_City/Oregon_home.html')

# Story #2: Create your model ----


def oregon_create(request):
    form = ActivityForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../display')
    content = {'form': form}
    return render(request, 'Oregon_City/Oregon_create.html', content)

# Story #3: Display all items from database ----


def oregon_display(request):
    activity = Activity.Entries.all()
    content = {'activity': activity}
    return render(request, 'Oregon_City/Oregon_display.html', content)

# Story #4: Details page -----


def oregon_details(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    content = {'activity': activity}
    return render(request, 'Oregon_City/Oregon_details.html', content)

# Story #5: Edit and Delete Functions -----


def oregon_update(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    form = ActivityForm(data=request.POST or None, instance=activity)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../display')
    content = {'form': form, 'activity': activity}
    return render(request, 'Oregon_City/Oregon_update.html', content)

# Story #6-(API Pt 1): Connect to API -----


def oregon_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('../../display')
    content = {'activity': activity}
    return render(request, 'Oregon_City/Oregon_delete.html', content)


def oregon_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"
    querystring = {"location": "oregon", "format": "json", "u": "f"}
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
    return render(request, 'Oregon_City/Oregon_api.html', content)

