from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurants
from .forms import RestaurantForm
import requests
import pprint
import json

def home(request):
    return render(request, 'NYC_Guide/nyc_home.html')

# add a restaurant
def add_rest(request):
    form= RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('nyc_guide_home')
    content = {'form': form}
    return render(request, 'NYC_Guide/add_rest.html', content)

# shows all restaurants from database
def all_rest(request):
    every_rest= Restaurants.Restaurants.all()
    context= {'every_rest': every_rest}
    return render(request, 'NYC_Guide/all_rest.html', context)

# shows details of one item
def details(request, restaurants_id):
    rest_request= get_object_or_404(Restaurants, pk=restaurants_id)
    context= {'rest_request': rest_request}
    return render(request, 'NYC_Guide/details.html', context)


# search a restaurant via search bar
def search_rest(request):
    if request.method == "POST":
        searched= request.POST['searched']
        restaurants= Restaurants.Restaurants.filter(restaurant_name__contains=searched)
        context= {'searched': searched, 'restaurants': restaurants}
        return render(request, 'NYC_Guide/search.html', context)
    else:
        return render(request, 'NYC_Guide/search.html', {})

# update a restaurant
def update_rest(request, restaurants_id):
    restaurant = get_object_or_404(Restaurants, pk=restaurants_id)
    form= RestaurantForm(request.POST or None, instance=restaurant)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('all_rest')
    context= {'form': form, 'restaurant': restaurant}
    return render(request, 'NYC_Guide/update.html', context)

# Delete a restaurant
def delete(request, restaurants_id):
    restaurant= get_object_or_404(Restaurants, pk=restaurants_id)
    form= RestaurantForm(request.POST or None, instance=restaurant)
    if request.method== "POST":
        restaurant.delete()
        return redirect('all_rest')
    context= {'form': form, 'restaurant': restaurant}
    return render(request, 'NYC_Guide/delete.html', context)

def yelp(request):
    restname= ' '
    restaurants= []

    if 'restname' in request.POST:
        restname= request.POST['restname']

        api_key= 'pmbFT7XHbjX6Ra3SSVspU_FyovRnPt7wBmMXJzH4Sa8MxVhRmZI7LsuSLFvS5v8JQp_TMK1qa-WP-T8uymCj3E2XrMZUgDXxhWm99fWazkuy_Uv35PHeZgb3VZLfYXYx'
        headers = {'Authorization': 'Bearer %s' % api_key}

        params = (
            ('term', restname),
            ('location', 'New York, NY'),
            ('limit', '10')
        )

        url = "https://api.yelp.com/v3/businesses/search"
        response = requests.get(url, headers=headers, params=params)
        parsed= response.json()
        rest_parsed=parsed['businesses']

        for businesses in rest_parsed:
            results= {
                'name': businesses['name'],
                'website': businesses['url'],
                'display_phone': businesses['display_phone'],
                'rating': businesses['rating'],
                # 'price': businesses['price'],
                'transactions': businesses['transactions'],
                'id': businesses['id']
            }
            restaurants.append(results)
    context={'restaurants': restaurants}
    print(context)
    return render(request, 'NYC_Guide/yelp.html', context)