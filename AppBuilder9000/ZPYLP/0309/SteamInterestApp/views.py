from django.shortcuts import render, redirect, get_object_or_404
from .forms import SteamInterestAppForm, SteamInterestAppBase
from django.core.paginator import Paginator

import json
import requests
from bs4 import BeautifulSoup


# Create your views here.
# Simple way to go to the home page.
def SIAHomePage(request):
    return render(request, 'SteamInterestApp/SIA_home.html')


def SIAAddEntry(request):
    # This is grabbing the modelform from our forms.py
    formentry = SteamInterestAppForm(request.POST or None)
    # If everything is good with the form, it'll save the form and redirect the user back to the home page.
    if formentry.is_valid():
        formentry.save()
        # Success! I tried adding an entry and it has appeared in the templates!
        # I should add in some form of confirmation so it's not ambiguous...
        return redirect('SIAAddSuccess')
    # If there's an issue with the form, it'll let the user know by printing the errors.
    else:
        print(formentry.errors)
    context = {
        'formentry': formentry
    }
    return render(request, 'SteamInterestApp/SIA_newEntry.html', context)


# Simple confirmation page after entering an entry.
def SIAAddConfirmation(request):
    return render(request, 'SteamInterestApp/SIA_entryConfirmation.html')


# Testing some code from memory/basic Django forms reading
def SIAViewAll(request):
    allentries = SteamInterestAppBase.objects.all()

    # Let's try adding a paginator! This allows us to control how many items are displayed per page.
    # I only have 3 entries in my db, so I'm gonna set it the limit to 1 for now.
    # All done testing! I'll set it to 2, just to showcase paginator purposes
    # When I add more entries, I'll change
    paginator = Paginator(allentries, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'SteamInterestApp/SIA_allEntries.html', context)


# We'll use this function to automatically populate a table with info from our templates!
def SIAViewEntry(request, pk):
    pk = int(pk)
    item = get_object_or_404(SteamInterestAppBase, pk=pk)

    # If the user chooses to save any updates to the form, it'll follow this if statement
    if request.method == 'POST':
        # Changing formset to formnistance for clarity
        forminstance = SteamInterestAppForm(request.POST, instance=item)
        if forminstance.is_valid():
            forminstance.save()
            return redirect('SIAEditSuccess')
    # If the user is initially pulling up the form, it'll follow this if statement
    else:
        forminstance = SteamInterestAppForm(instance=item)

    # This part saves the info as a dictionary we can pass through to the template
    context = {
        'item': forminstance,
        # Alright! I was having trouble grabbing the id of the model object passed through this context.
        # As a result, I just added a kvp to this context dictionary to include the pk!
        # We'll use this with the JS delete button to specify which object we wish to delete.
        'primarykey': pk
    }
    return render(request, 'SteamInterestApp/SIA_viewEntry.html', context)


# Simple confirmation page after editing an entry
def SIAEditConfirmation(request):
    return render(request, 'SteamInterestApp/SIA_editEntryConfirmation.html')


# Now we'll add a view for deleting an entry!
def SIADeleteEntry(request, pk):
    pk = int(pk)
    item = get_object_or_404(SteamInterestAppBase, pk=pk)
    item.delete()

    context = {
        'item': item
    }

    # Slight roadblock with this function not returning correctly!
    # Turns out I'm a dingus and wasn't using the right html template
    # I was just looping the function back to itself, which doesn't make sense haha. It's good now!
    return render(request, 'SteamInterestApp/SIA_deleteSuccess.html', context)


# Simple Views function to return our data scrape test page
def SIADataScrapeTest(request):

    # Ok, here's the plan!
    # Data scraping from Steam is going to be a little bit harder. In general, we would want to grab from
    # a fixed content website. Since STEAM dynamically generates so much of their content, it would be hard
    # to accurately scrape. Instead, I'm going to look for some gaming news website that has a top 10 list
    # for 2020 and scrape from there. I do still want STEAM connectivity, so I'm going to do research on using
    # one of the STEAM APIs instead. Theoretically, that should cover all bases!

    gamespot_page = requests.get("https://www.gamespot.com/articles/gamespots-best-game-of-2020-nominees/1100-6485319/")
    gamespot_soup = BeautifulSoup(gamespot_page.content, 'html.parser')
    gamespot_titles = gamespot_soup.select("div.content-entity-body h2")
    gamespot_titles_isolated = [titles.get_text() for titles in gamespot_titles]
    gamespot_links = gamespot_soup.select("div.content-entity-body p a")
    gamespot_links_isolated = [links.get_text() for links in gamespot_links]

    gamespot_titles_isolated_cleaned = [item for item in gamespot_titles_isolated if item != " "]


    # Let's make a list with just the nominees!
    # What we'll do is set a string that is present in all the game page links, which we see below:
    nominee_string = "/articles/best-games-of-2020"
    # We'll create an empty list that we'll populate as we iterate through our soup.
    nominee_list = []
    # We're going to look at each item in the gamespot_links soup
    for items in gamespot_links:
        # We then check if the string above is found in the href of our soup item.
        # The reason why we check if it's greater than -1 is because find returns the index of the string.
        # If the string is -1, that means the string wasn't found. Thus, this if statement finds all instances
        # of links that contain our nominee string above!
        if items['href'].find(nominee_string) > -1:
            nominee_list.append(items['href'])

    # Whoever set up this page did not follow the same naming convention for FFVII Remake...
    # As a result, I have to manually set this one
    nominee_list[3] = "https://www.gamespot.com/articles/best-games-of-2020-final-fantasy-7-remake/1100-6485362/"

    # Let's see if I can create a loop counter for index reference so I can loop through both
    numeric_list = [0, 1, 2, 3, 4, 5]
    # Nope! Can't pass a context dictionary an index... This does not work!

    # What if I combine both lists of interest into a dictionary and pass it as a context variable?

    my_dictionary = {}
    for i in range(0, 9):
        my_dictionary.update({gamespot_titles_isolated_cleaned[i]: nominee_list[i]})

    # Ah my goodness, finally!!!! I was not using my dictionary syntax correctly...
    # I had set the values to key and had nested dictionaries,
    # but that was causing calling issues. It's hard since you can't pass a variable
    # to a dictionary you're calling in a template.
    # With this new dictionary, though, we can iterate in the template, giving us the
    # appropriate tds for the game title and links

    context = {
        'gamespot_titles': gamespot_titles,
        'gamespot_titles_isolated': gamespot_titles_isolated,
        'gamespot_links': gamespot_links,
        'gamespot_links_isolated': gamespot_links_isolated,
        'nominee_list': nominee_list,
        'gamespot_titles_isolated_cleaned': gamespot_titles_isolated_cleaned,
        'numeric_list': numeric_list,
        'my_dictionary': my_dictionary,
    }

    return render(request, 'SteamInterestApp/SIA_dataScrapeTest.html', context)


# Let's see if we can grab some of the free API Data/non-key data for TF2!
# Success! Now we'll have this views function take a simple user input to call relevant info
# for the game ID entered!
def SIASteamAPITest(request, pk):
    steam_id = int(pk)
    steam_api = requests.get("http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={}&count=5&maxlength=200&format=json".format(steam_id))
    steam_success = steam_api.status_code
    pretty_api = json.dumps(steam_api.json(), sort_keys=True, indent=4)

    number_of_stories = 0

    if steam_success == 200:
        api_newsitems = steam_api.json()['appnews']['newsitems']
        number_of_stories = steam_api.json()['appnews']['count']


        # Or maybe we can bypass it all together?
        print(pretty_api)
        api_full_news = {}
        upper_range = len(api_newsitems)
        for i in range(0, upper_range):
            api_full_news[i] = []
            a = api_newsitems[i]['title']
            b = api_newsitems[i]['url']
            c = api_newsitems[i]['contents']
            api_full_news[i] = [a, b, c]
    else:
        api_newsitems = {}
        api_full_news = {}

    context = {
        'steam_success': steam_success,
        'steam_api': steam_api,
        'pretty_api': pretty_api,
        'api_newsitems': api_newsitems,
        'api_full_news': api_full_news,
        'number_of_stories': number_of_stories,
    }

    return render(request, 'SteamInterestApp/SIA_SteamAPITest.html', context)


# You know, this should probably be above the other function since chronologically users will encounter this page first
# I'm going to keep it like this for now since it's the order I'm programming in haha.
def SIASteamGameIDEntry(request):
    return render(request, 'SteamInterestApp/SIA_SteamAPICall.html')