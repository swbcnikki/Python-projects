from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, DishForm, SearchForm
from .models import Restaurant, Dish
from operator import attrgetter
import argparse
import json
import pprint
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode



def MyThai_home(request):
    return render(request, 'MyThai/MyThai_home.html')


def new_restaurant(request):
    # Store Restaurant form as form
    form = RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        # If form is valid save and return to dishes page.
        if form.is_valid():
            form.save()
            return redirect('MyThai_my_restaurants')
        else:
            # If form isn't valid return to the add page with the content entered.
            content = {'form': form}
            return render(request, 'MyThai/MyThai_add_restaurant.html', content)
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add_restaurant.html', content)


def new_dish(request):
    form = DishForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MyThai_my_restaurants')
        else:
            content = {'form': form}
            return render(request, 'MyThai/MyThai_add_dish.html', content)
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add_dish.html', content)


def my_restaurants_view(request):
    # Store objects from DB in object as dict.
    dish_list = Dish.objects.all()
    # GET search & sort data for table
    get_dish_query = request.GET.get('get_dish')
    my_sort = request.GET.get('dishes')

    if is_valid_query(get_dish_query):  # If 'is valid' = True, filter the queryset
        dish_list = dish_list.filter(
            # Turn filters into objects to pass to filter()
            Q(dishName__icontains=get_dish_query) |  # Search by dish name & restaurant name
            Q(restaurant__name__icontains=get_dish_query)).distinct()  # Returning only distinct entries

    dish_list = my_sorted(dish_list, my_sort)  # Sort qs
    paginator = Paginator(dish_list, 10)  # Create paginator object with 10 restaurants per page
    page = request.GET.get('page')  # Store paginator object with current page
    dishes = paginator.get_page(page)

    context = {'dishes': dishes}
    return render(request, 'MyThai/MyThai_my_dishes.html', context)


def is_valid_query(param):
    return param != '' and param is not None  # Makes sure search is valid query, if not return false


def my_sorted(dish_list, my_sort):
    if my_sort == 'rating':  # If sorted by rating, reverse so highest goes at the top.
        asc = True
    elif my_sort is None:  # If my_sort is None, sort by dish name
        my_sort = 'dishName'
        asc = False
    else:
        asc = False
    dish_list = sorted(dish_list, key=attrgetter(my_sort), reverse=asc)  # Sort dict by model attribute = 'my_sort'
    return dish_list


def details(request, pk):
    pk = int(pk)
    # Get object with pk
    dish = get_object_or_404(Dish, pk=pk)
    context = {'dish': dish}
    return render(request, 'MyThai/MyThai_details.html', context)


def restaurant_details(request, pk):
    pk = int(pk)
    restaurant = get_object_or_404(Restaurant, pk=pk)
    context = {'restaurant': restaurant}
    return render(request, 'MyThai/MyThai_rest_details.html', context)


def dish_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Dish, pk=pk)
    form = DishForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        save_edit(form)  # If form is valid, save and redirect to all dishes page
        return redirect('MyThai_my_restaurants')
    else:
        return render(request, 'MyThai/MyThai_dish_edit.html', {'form': form})


def restaurant_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Restaurant, pk=pk)
    form = RestaurantForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        save_edit(form)
        return redirect('MyThai_my_restaurants')
    else:
        return render(request, 'MyThai/MyThai_rest_edit.html', {'form': form})


def save_edit(form):
    # Save valid forms, else print errors.
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
    else:
        print(form.errors)


def dish_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('MyThai_my_restaurants')
    context = {"item": item}
    return render(request, "MyThai/MyThai_delete.html", context)


def restaurant_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('MyThai_my_restaurants')
    context = {"item": item}
    return render(request, "MyThai/MyThai_delete.html", context)


def dish_confirmed(request):
    if request.method == 'POST':
        form = DishForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('MyThai_my_restaurants')
        else:
            return redirect('MyThai_my_restaurants')


def restaurant_confirmed(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('MyThai_my_restaurants')
        else:
            return redirect('MyThai_my_restaurants')


def restaurant_search(request):
    # Pass form to search view
    context = {'form': SearchForm}
    return render(request, 'MyThai/MyThai_api_search.html', context)


def restaurant_results(request):
    """
    API documentation
    https://www.yelp.com/developers/documentation/v3/business_search

    *   REMOVE API_KEY  *
    -Store in settings.py
    -Use decouple
    Do NOT release API key
    """
    API_KEY = 'QEFNe77PDTdEruX0EeI91uyTUrJg4NG0guiDraZ8pFkyeED1XUTvlv1zTcOgYmoTVxxHCGCMGUVQs5XRwxM4CxOrUTBjECcZTwsMwF3phWshUH_tdRL4hDseyaqBYHYx'

    if request.method == 'POST':
        # Get user's search input from SearchForm
        form = SearchForm(request.POST or None)

        if form.is_valid():
            # Return term from form as dict, store as term
            term = form.cleaned_data['search_term']
            response = api_search(API_KEY, term)
            search_data = response.json()

            search_businesses = search_data['businesses'][0]
            business_location = search_businesses['location']
            pprint.pprint(search_businesses, indent=3)

            context = {'name': search_businesses['name'],
                       'display_phone': search_businesses['display_phone'],
                       'rating': search_businesses['rating'],
                       'is_closed': search_businesses['is_closed'],
                       'address1': business_location['address1'],
                       'city': business_location['city'],
                       'zip_code': business_location['zip_code']
                       }

            return render(request, 'MyThai/MyThai_api_results.html', context)

        else:
            return redirect('MyThai_search')


def api_search(api_key, term):
    # API search path params
    API_HOST = 'https://api.yelp.com'
    SEARCH_PATH = '/v3/businesses/search'
    SEARCH_LIMIT = 1
    SEARCH_CATEGORY = 'Thai'
    SEARCH_LOCATION = 'Portland, OR'

    # URL search params as dict
    url_params = {
        'term': term.replace(' ', '+'),             # Remove spaces from params
        'location': SEARCH_LOCATION.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'categories': SEARCH_CATEGORY
    }

    return api_request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def api_request(host, path, api_key, url_params=None):
    # If url_params is None store empty dict
    url_params = url_params or {}
    # Combine host and path to make url
    url = '{}{}'.format(host, quote(path.encode('utf8')))
    # Authorization header for API
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    # Construct API get request
    response = requests.request('GET', url, headers=headers, params=url_params)
    # Return dict response as json
    return response
