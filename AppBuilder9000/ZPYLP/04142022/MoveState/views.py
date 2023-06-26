from django.shortcuts import render, get_object_or_404, redirect

from .form import movestateForm
from .models import Movestate
import requests
import json
from bs4 import BeautifulSoup


def movestate_home(request):
    return render(request, "MoveState/movestate_home.html")


def add_state(request):
    form = movestateForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movestate_home')
    else:
        print(form.errors)
        form = movestateForm()
    context = {
        'form': form,
    }
    return render(request, 'MoveState/add_state.html', context)


def list_state(request):
    list = Movestate.Movers.all()
    return render(request, 'MoveState/list_state.html', {'list': list})


def movestate_details(request, pk):
    details = get_object_or_404(Movestate, pk=pk)
    context = {'details': details}
    return render(request, 'MoveState/movestate_details.html', context)


def movestate_delete(request, pk):
    item = get_object_or_404(Movestate, pk=pk)
    form = movestateForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('list_state')
    context = {"item": item, 'form': form}
    return render(request, "MoveState/movestate_delete.html", context)


def movestate(data, instance):
    pass


def movestate_edit(request, pk):
    item = get_object_or_404(Movestate, pk=pk)
    form = movestateForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('list_state')
        else:
            print(form.errors)
    else:
        return render(request, 'MoveState/movestate_edit.html', {'form': form})

# bs section
def movestate_history(request):
    movestate_list = []
    page = requests.get("https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_net_migration")
    soup = BeautifulSoup(page.content, 'html.parser')
    previous_state = soup.find('div', class_='mw-parser-output')
    tbody = previous_state.find('tbody')
    movestate = tbody.find_all('tr')
    for tr in movestate:
        td = tr.find_all('td')
        row = [i.text for i in td]
        cells = row
        movestate_list.append(cells)
    print(movestate_list)
    context = {'movestate_list': movestate_list}

    return render(request, 'MoveState/movestate_history.html', context)

# api section
def movestate_api(request):
    city_name = []
    population = []

    url = "https://countries-cities.p.rapidapi.com/location/country/US/city/list"

    querystring = {"page": "1", "per_page": "20", "population": "601000"}

    headers = {
        'x-rapidapi-host': "countries-cities.p.rapidapi.com",
        'x-rapidapi-key': "72da559dc6msha2b6fe581591e33p11e66cjsn7a377520e5e4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    api_response = json.loads(response.text)
    cities = api_response['cities']
    for i in cities:
        name = i["name"]
        city_name.append(name)
    for y in cities:
        pop = y['population']
        population.append(pop)
    print(city_name)
    print(population)
    context = {'city_name': city_name, 'population': population}
    return render(request, 'MoveState/movestate_api.html', context)