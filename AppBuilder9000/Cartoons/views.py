from django.shortcuts import render, redirect, get_object_or_404
from .forms import CartoonForm
from .models import Cartoon, Definition
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.
""" HOME, CREATE, DISPLAY, UPDATE, DELETE CARTOON SECTION """
# This is so the user can go back to the home page when clicking "home" on the navbar.
def Cartoons(request):
    return render(request, 'Cartoons/Cartoons_home.html')

# Gets the data from the CartoonForm and saves it into the DB if request method == POST and the form info is valid.
# Redirects to the list page after submitting.
def CreateCartoon(request):
    form = CartoonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Cartoons_list')
    context = {'form': form}
    return render(request, "Cartoons/Cartoons_create.html", context)

# Gets data from models.py and then have that information returned and displayed onto the cartoons list page.
def DisplayCartoons(request):
    cartoon_list = Cartoon.Cartoons.all().order_by("premier_date")  # Orders by premier date in numerical/date order.
    context = {'cartoon_list': cartoon_list}
    return render(request, 'Cartoons/Cartoons_list.html', context)

# Gets the primary key from the DB and uses it to display more details after the cartoon name is selected.
def DisplayDetails(request, pk):
    item = get_object_or_404(Cartoon, pk=pk)
    context = {'item': item}
    return render(request, 'Cartoons/Cartoons_details.html', context)

# This function passes the user to the delete-confirmation page where they can confirm or deny deleting an item from DB.
# If they confirm, then item is deleted, and they are redirected to the list page.
def DeleteItem(request, pk):
    context = {}
    item = get_object_or_404(Cartoon, pk=pk)

    if request.method == "POST":
        item.delete()
        return redirect("Cartoons_list")

    return render(request, "Cartoons/Cartoons_delete.html", context)

# Gets the form from our model and makes sure that the data the user inputted is valid.
# If valid, saves the data  and then redirects back to the list page.
def UpdateItem(request, pk):
    item = Cartoon.Cartoons.get(pk=pk)
    form = CartoonForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('Cartoons_list')

    context = {'item': item, 'form': form}
    return render(request, 'Cartoons/Cartoons_up_date.html', context)

""" BEAUTIFULSOUP SECTION """

""" 
The below code scrapes the number and titles of the cartoons from indiewires website where they are ranking the best 
animated series of all time. There are over 60 cartoons in the list and about 10 are displayed per page. I selected the 
specific page that named the top 10 cartoons. The titles were all under <h3> tags in the html code.
"""
def CartoonScrape(request):
    # Create empty list.
    top_cartoons = []
    # Set up BeautifulSoup.
    source = requests.get("https://www.indiewire.com/feature/best-animated-series-all-time-cartoons-anime-tv-1202021835/5/")
    bs = BeautifulSoup(source.content, 'html.parser')
    # Get all the h3 tags under the div 'entry-content' from source site.
    rankings = bs.find('div', class_='entry-content')
    rank = rankings.find_all('h3')
    # For loop through the h3 tags but in reverse order (because they are displayed reversed on the source page).
    for h3 in reversed(rank):
        titles = h3.text
        top_cartoons.append(titles)
    # Delete indexes 8-9 which are irrelevant h3 tags.
    del top_cartoons[8:10]

    context = {'top_cartoons': top_cartoons}
    return render(request, 'Cartoons/Cartoons_rankings.html', context)

""" 
The below code scrapes the ranking/rating/titles of the top 100 animated movies on rotten tomatoes website.
"""
def MovieScrape(request):
    # Create empty list.
    top_movies = []
    # Set up BeautifulSoup.
    source = requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
    bs = BeautifulSoup(source.content, 'html.parser')
    # Get all the "a" tags under the table 'table' from source site.
    rankings = bs.find('table', class_='table')
    rank = rankings.find_all('tr')
    # For loop that iterates through all the "a" tags.
    for tr in rank:
        titles = tr.text
        top_movies.append(titles)
    # Delete index 0, which is not needed.
    del top_movies[0]

    context = {'top_movies': top_movies}
    return render(request, 'Cartoons/Cartoons_movies.html', context)

""" OXFORD API SECTION """

""" 
The below code connects to the Oxford Dictionary API and allows users to search any word within the dictionary to
view the definition. I initially wanted to find an API that was relevant to Cartoons but I couldn't find anything that
would have added a cool function. I went ahead and added the dictionary because I thought the idea/function was useful 
and it was also good for practice purposes.
"""
def OxfordAPI(request):
    # Set up API connection.
    app_id = '591386c7'
    app_key = 'ea768fd0e3d3a96ec8b39d08533c1f36'
    language = 'en-us'
    fields = 'definitions'
    strictMatch = 'false'
    # Create empty list.
    definition=[]
    if request.method=='POST': # If/else statement to make sure that the user input isn't blank.
        value = request.POST['word_id'].lower()
        # If input is blank it will display this message.
        if value == "":
            messages.info(request, 'Please enter a search term')
        else:  # else run the code below
            url ='https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + value + '?fields=' + fields + '&strictMatch=' + strictMatch;
            info=requests.get(url,headers={'app_id':app_id, 'app_key':app_key})
            oxford_info=info.json()
            result=oxford_info['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
            definition.append(result)

            # Added this section to save the users search in a new DB (definitions)
            save_definition = Definition.Definitions.create(
                value=value,
                definition=result
            )
            save_definition.save()

        context={'value':value,'definition':definition}
        return render(request, 'Cartoons/Cartoons_api.html', context)
    else:
        return render(request, 'Cartoons/Cartoons_api.html')


# Gets data from models.py and then haves that information returned and displayed onto the definitions page.
def DisplayDefinitions(request):
    definition_list = Definition.Definitions.all().order_by("value")  # Orders by value in alphabetical order.
    context = {'definition_list': definition_list}
    return render(request, 'Cartoons/Cartoons_definitions.html', context)


