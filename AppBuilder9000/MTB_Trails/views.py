import pprint

from django.shortcuts import render, get_object_or_404, redirect
from .forms import TrailReviewForm
from .models import ReviewTrail
from bs4 import BeautifulSoup
import requests
import json


def mtb_trails_home(request):
    return render(request, 'MTB_Trails/mtb_trails_home.html')


# User data from form to be saved and then user redirected to submitted_review
def mtb_trails_review(request):
    # If this is a POST request we need to process the form data
    form = TrailReviewForm(data=request.POST or None)
    if request.method == 'POST':
        # Check if data is valid:
        if form.is_valid():
            form.save()
            # Process data in form.cleaned_data as required
            # Redirect to new URL
            return redirect('submitted_review')
    else:
        form = TrailReviewForm()
    context = {'form': form}
    return render(request, 'MTB_Trails/mtb_trails_review.html', context)


# Simple rendering for success review submission
def submitted_review(request):
    return render(request, 'MTB_Trails/submitted_review.html')


# View for user-submitted reviews
def existing_reviews(request):
    trails = ReviewTrail.objects.all()
    return render(request, 'MTB_Trails/existing_reviews.html', {'trails': trails})


# View for detailed review page
def review_details(request, pk):
    trail = ReviewTrail.objects.get(pk=pk)
    return render(request, 'MTB_Trails/review_details.html', {'trail':trail})


# View for updating or deleting review (page has modal that'll link to the delete_trail view below).
def edit_or_delete(request, pk):
    trail = get_object_or_404(ReviewTrail, pk=pk)
    form = TrailReviewForm(instance=trail)
    if request.method == 'POST':
        form = TrailReviewForm(request.POST, instance=trail)
        # Check if data is valid:
        if form.is_valid():
            form.save()
            # Process data in form.cleaned_data as required
            # Redirect to new URL
            return redirect('submitted_review')
        # Cindy, I don't know why, but changing dictionary to 'trail' won't load form in webpage.
    context = {'form': form,
               'trail': trail}
    return render(request, 'MTB_Trails/edit_or_delete.html', context)


# View for deleting a review.
def delete_trail(request, pk):
    trail = get_object_or_404(ReviewTrail, pk=pk)
    context = {'trail': trail}
    trail.delete()
    return redirect('existing_reviews')


# Beautiful Soup webpage scraping.
# View for scraping our selected page.
def top_mtb(request):
    # Empty list for use in for loop.
    top_bikes = []
    # Empty list for use in for loop.
    bike_desc = []
    # Empty list for use in last for loop. This loop concatenates the other two lists.
    full_bike_desc = []
    # URL to be scraped.
    page = requests.get('https://www.outdoorgearlab.com/topics/biking/best-mountain-bike')
    # Setting soup object using the particular html parser.
    soup = BeautifulSoup(page.content, 'html.parser')
    # Accessing second 'articletext' class as there are two used (and we want the second only).
    parent = soup.find_all('div', class_='articletext')[1:]
    # This for loop iterates through the 'h2' tags within the class 'articletext'.
    # They are put into the blank 'bike_desc' list.
    for i in parent:
        desc = i.find_all('h2')
        for j in desc:
            desc_txt = j.text
            bike_desc.append(desc_txt)

    # This second body of the for loop iterates through the 'h3' tags within 'articletext'.
    # They are put into the blank 'top_bikes' list.
        bike = i.find_all('h3')
        for x in bike:
            bike_txt = x.text
            top_bikes.append(bike_txt)
    # New list containing only the elements we want from both lists.
    new_desc_list = bike_desc[0:8]
    new_top_bike_list = top_bikes[0:8]

    # Joining together list elements since we have two separate lists above.
    z = 0
    for desc in new_desc_list:
        bike_model = new_desc_list[0 + z] + ': ' + new_top_bike_list[0 + z]
        full_bike_desc.append(bike_model)
        z += 1

    context = {'full_bike_desc': full_bike_desc}
    return render(request, 'MTB_Trails/top_mtb.html', context)


# View for MTB Project API
def trail_api(request):
    # API code from https://rapidapi.com/trailapi/api/trailapi/
    url = "https://trailapi-trailapi.p.rapidapi.com/trails/explore/"

    # Latitude and longitude required. 'per_page' and 'radius' optional.
    parameters = {"lat": "39", "lon": "-106", "per_page": "300", "radius": "100"}
    headers = {
        "X-RapidAPI-Host": "trailapi-trailapi.p.rapidapi.com",
        "X-RapidAPI-Key": "e3b28ce81fmshbcd98af11e9812dp1487c5jsnaf6f45c8d994"
    }
    response = requests.request("GET", url, headers=headers, params=parameters)
    json_response = response.json()

    # Empty lists to populate with data we want to pull from the API.
    trail_name_list = []
    trail_desc_list = []
    trail_city_list = []
    trail_difficulty_list = []

    # Populating all lists except 'trail_list'.
    for item in json_response['data']:
        trail_name_list.append(item['name'])
        trail_desc_list.append(item['description'])
        trail_city_list.append(item['city'])
        trail_difficulty_list.append(item['difficulty'])

    trail_list = zip(trail_name_list, trail_desc_list, trail_city_list, trail_difficulty_list)

    context = {'trail_list': trail_list}
    return render(request, 'MTB_Trails/trail_api.html', context)























