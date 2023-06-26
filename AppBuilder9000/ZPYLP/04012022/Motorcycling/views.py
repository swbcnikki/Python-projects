import json

from django.shortcuts import render, redirect, get_object_or_404
from .models import Motorcycle, Route
from .forms import MotorcycleForm, RouteForm
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import requests



# This creates the function for the admin console.
def admin_console(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, 'products/products_page.html', {'motorcycles': Motorcycle})


# This creates the function that leads the user to the home page.
def motorcycling_home(request):
    return render(request, 'Motorcycling/motorcycling_home.html')

# This is the function that lets the user create a motorcycle that is saved to the database.
def create_motorcycle(request):
    form = MotorcycleForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('rate_motorcycle')
        else:
            print(form.errors)
            form = MotorcycleForm()
    context = {'form': form}
    return render(request, 'Motorcycling/rate_motorcycle.html', context)

# This is the function that lets the user create a simple route that is saved to the database.
def create_route(request):
    form = RouteForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('rate_route')
        else:
            print(form.errors)
            form = RouteForm()
    context = {'form': form}
    return render(request, 'Motorcycling/rate_route.html', context)

# This function calls all the motorcycles in the database and displays them to html page
def all_motorcycles(request):
    motorcycle_list = Motorcycle.objects.all()
    return render(request, 'Motorcycling/list_motorcycles.html', {'motorcycle_list': motorcycle_list})


# This allows the user to delete an item in the database
def delete_motorcycle_admin(request, pk):
    item = get_object_or_404(Motorcycle, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list_motorcycles.html')
    context = {'Motorcycle': Motorcycle}
    return render(request, 'Motorcycling/list_motorcycles.html', context)

# This function will list all the saved routes
def all_routes(request):
    route_list = Route.objects.all()
    return render(request, 'Motorcycling/list_routes.html', {'route_list': route_list})


# This function will query the database and return a result per the user's request.
def motorcycle_details(request, pk):
    motorcycle_detail = get_object_or_404(Motorcycle, pk=pk)
    return render(request, 'Motorcycling/motorcycle_details.html', {'motorcycle_detail': motorcycle_detail})


# This function shows specific route data to the user
def route_details(request, pk):
    route_detail = get_object_or_404(Route, pk=pk)
    return render(request, 'Motorcycling/route_details.html', {'route_detail': route_detail})


# This function will let a user edit their data on the motorcycle
def update_motorcycle(request, pk):
    edit_motorcycle = get_object_or_404(Motorcycle, pk=pk)
    form = MotorcycleForm(data=request.POST or None, instance=edit_motorcycle)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_motorcycles')
    return render(request, 'Motorcycling/update_motorcycle.html', {'edit_motorcycle': edit_motorcycle, 'form': form})


# This function allows the user to delete the item in the database
def delete_motorcycle(request, pk):
    delete_user_motorcycle = get_object_or_404(Motorcycle, pk=pk)
    form = MotorcycleForm(data=request.POST or None, instance=delete_user_motorcycle)
    if request.method == 'POST':
        delete_user_motorcycle.delete()
        return redirect('list_motorcycles')
    return render(request, 'Motorcycling/delete_motorcycle.html',
                  {'delete_user_motorcycle': delete_user_motorcycle, 'form': form})


# This will allow the user to make updates to the database
def update_route(request, pk):
    route = get_object_or_404(Route, pk=pk)
    form = RouteForm(data=request.POST or None, instance=route)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_routes')
    return render(request, 'Motorcycling/update_route.html', {'route': route, 'form': form})


# This will allow the user to make updates to the database
def delete_route(request, pk):
    delete_user_route = get_object_or_404(Route, pk=pk)
    form = RouteForm(data=request.POST or None, instance=delete_user_route)
    if request.method == 'POST':
        delete_user_route.delete()
        return redirect('list_routes')
    return render(request, 'Motorcycling/delete_route.html', {'delete_user_route': delete_user_route, 'form': form})

# This uses BeautifulSoup to scrape a website for data about motorcycles
def BS_scraper(request):
    cycle = []
    # Load in the webpage
    page = requests.get("https://hiconsumption.com/best-motorcycles-of-all-time/")
    # Convert to a BeautifulSoup object
    soup = BeautifulSoup(page.content, 'html.parser')
    # Search for specific elements in the website, narrowed to its parent class
    div = soup.find('div', class_='wp-content')
    best_bike = div.find_all('h3')
    # iterate through the results to get the list of motorcycles
    for i in best_bike:
        name = i.text
    # Grabbing just the names of the resulting motorcycles
        cycle.append(name)
    print(cycle)
    return render(request, 'Motorcycling/motorcycling_scraper.html', {'cycle': cycle})


# This is an API that generates a random city near the user they can ride to "think Magic-8 Ball"
def motorcycling_API(request):
    info = []
    distance = []
    population = []



    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/locations/40.7608-111.8910/nearbyCities"

    querystring = {"radius": "100"}

    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "bfa3041daemsh311c181100b3f88p1405fbjsn18f663313ac1"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    random_city = json.loads(response.text)

    destination_city = random_city['data']
    for i in destination_city:
        city_name = i['city']
        info.append(city_name)
    for j in destination_city:
        city_distance = j['distance']
        distance.append(city_distance)
    for k in destination_city:
        city_population = k['population']
        population.append(city_population)


    print(info, distance, population)


    return render(request, 'Motorcycling/motorcycling_API.html',
                  {'info': info, 'distance': distance, 'population': population})
