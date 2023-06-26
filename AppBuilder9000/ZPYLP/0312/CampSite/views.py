from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import CampsiteForm, SearchForm
from .models import Campsite
from bs4 import BeautifulSoup
import requests
import json


def campsite_home(request):
    return render(request, 'CampSite/CampSite_home.html')


# Add a new campsite to the dB
def add_campsite(request):
    form = CampsiteForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        print('method is POST')
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('browse')
    context = {'form': form}
    return render(request, 'CampSite/add_campsite.html', context)


# Show list of all campsites in dB
def browse(request):
    campsite = Campsite.Campsites.all()
    # Set up pagination
    paginator = Paginator(campsite, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'CampSite/browse_campsites.html', context)


# Get campsite details from browse page
def campsite_details(request, campsite_id):
    campsite = get_object_or_404(Campsite, pk=campsite_id)
    context = {'campsite': campsite}
    return render(request, 'Campsite/campsite_details.html', context)


# Edit campsite from details page
def edit_campsite(request, campsite_id):
    # Get campsite object from dB via id
    campsite = get_object_or_404(Campsite, pk=campsite_id)
    if request.method == 'POST':
        # Display info for campsite instance as form
        form = CampsiteForm(data=request.POST, instance=campsite)
        if form.is_valid():
            # Save changes if form is valid and redirect back to details page (w/ updates)
            form.save()
            return redirect('campsite_details', campsite.id)
    else:
        form = CampsiteForm(instance=campsite)
    context = {'form': form}
    return render(request, 'CampSite/edit_campsite.html', context)


def delete_campsite(request, campsite_id):
    campsite = get_object_or_404(Campsite, pk=campsite_id)
    campsite.delete()
    return redirect('browse')


def bs_scrape(request):
    # Get forest service page with list of campsites
    page = requests.get("https://www.fs.usda.gov/activity/mthood/recreation/camping-cabins/?recid=52770&actid=29")
    # Use Beautiful Soup to parse html
    soup = BeautifulSoup(page.content, 'html.parser')
    # Using index, single out list of campsites
    campsites_list = list(soup.find_all('ul'))[5]
    # Find all 'a' elements in campsites_list to get campsite names and links
    campsites = campsites_list.find_all('a')
    # Array to hold all info about all sites
    sites_info = []

    for i in range(len(campsites)):
        # Dictionary to hold info about individual sites
        site_details = {}
        # Single out names of campsites and make them values of dictionary key 'name'
        site_details['name'] = campsites[i].get_text()
        # Set campsite type depending on text in site name
        if 'Campground' in site_details['name']:
            site_type = 'Developed'
            site_access = 'Drive-Up'
        elif 'Trail' in site_details['name']:
            site_type = 'Dispersed'
            site_access = 'Hike-in'
        else:
            site_type = ''
            site_access = ''
        site_details['access'] = site_access
        # Set campsite type as values for dictionary key 'type'
        site_details['type'] = site_type
        # Single out link to each campsite
        site_link = campsites[i].get('href')
        # Make sure campsite links are the full link, try/catch for TypeError
        try:
            if 'http://www.fs.usda.gov' in site_link:
                site_full_link = site_link
            else:
                site_full_link = 'http://www.fs.usda.gov' + site_link
        except TypeError:
            pass
        # Set full links to sites as values of dictionary key 'link'
        site_details['full_link'] = site_full_link
        # Add site details to sites_info array
        sites_info.append(site_details)

    # Set up pagination
    paginator = Paginator(sites_info, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Dictionary to display NF campsite info on page
    context = {
        'page_obj': page_obj
    }
    print(context)

    return render(request, 'CampSite/CampSite_nationalForest.html', context)


def search_api(request):
    # variable to hold value of user input
    user_input = []
    form = SearchForm(request.POST or None)
    # Process form data
    if request.method == 'POST':
        # Check from validity
        if form.is_valid():
            # Set value of user input to a variable, make lower case for error avoidance
            search_terms = request.POST.get('searchTerms').lower()
            # Add value of user input to variable for use outside this function
            user_input.append(search_terms)
            print(user_input)
    else:
        form = SearchForm()
    if len(user_input) == 0:
        context = {'form': form}

        return render(request, 'CampSite/CampSite_searchAPI.html', context)
    else:
        # Split user input string into individual words
        split_input = user_input[0].split()
        # If statement for one-word input to get park code
        park_code = []
        if len(split_input) == 1:
            np_name = split_input[0]
            np_code = np_name[0:4]
            park_code.append(np_code)
        # If statement for multi-word user input to get park code
        elif len(split_input) >= 2:
            np_name = split_input[0:2]
            first_name = np_name[0]
            second_name = np_name[1]
            np_code = first_name[0:2] + second_name[0:2]
            park_code.append(np_code)
        park_code = park_code[0]
        key = 'mJEOpAw6zq2D9gtJbecpvFkPecgRhHkf8HEWRLDH'
        path = 'https://developer.nps.gov'
        response = requests.get('{}/api/v1/campgrounds?parkCode={}&api_key={}'.format(path, park_code, key))
        all_sites = response.json()
        all_sites_pretty = json.dumps(all_sites, sort_keys=True, indent=4)

        # From JSON I will pull out campsite name, description, directions, and lat/long(to display map)
        print(all_sites_pretty)

        context = {'form': form}

        return render(request, 'CampSite/CampSite_searchAPI.html', context)

