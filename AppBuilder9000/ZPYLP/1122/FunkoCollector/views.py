from django.shortcuts import render, redirect
from requests import request

from .models import FunkoPopName
from .forms import CollectionForm
from django.http import HttpResponseRedirect
from django.db.models import Q
import requests
from bs4 import BeautifulSoup



def funkocollectorhome(request):
    return render(request, 'funkocollectorhome.html')

# function for rendering a form for adding to the CollectionForm database from the web page addcollection.html


def addcollection(request):
    submitted = False
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('addcollection?submitted=True')
    else:
        form = CollectionForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addcollection.html', {'form': form, 'submitted': submitted})

# function for rendering a information saved from the CollectionForm database to the web page collection.html


def collection(request):
    collectionpop = FunkoPopName.objects.all()
    return render(request, 'collection.html', {'collectionpop': collectionpop})

# function for rendering an information page from a search box in the nav bar.  Will render all information from a
# database from a search criteria inputted into the search box.


def searchcollection(request):
    if request.method == "POST":

        searched = request.POST['searched']
        pops = FunkoPopName.objects.filter(Q(name__contains=searched) | Q(size__contains=searched) |
                                           Q(fandome__contains=searched) | Q(chase__contains=searched) |
                                           Q(purchase_price__contains=searched) | Q(value__contains=searched))

        return render(request, 'searchcollection.html', {'searched': searched, 'pops': pops})
    else:
        return render(request, 'searchcollection.html', {})

# function for rendering a details page from a clickable link found by the pk-id of an object in the database
# to display the details of that one object.


def detailscollection(request, funkopopname_id):
    detailspop = FunkoPopName.objects.get(pk=funkopopname_id)
    return render(request, 'detailscollection.html', {'detailspop': detailspop})

# function for rendering a update page form from a button on the  collection table for each object found by the pk-id
# in the database in a form that shows all the data from the database in the form.  You can then change the information
# in each field or just one field.  Click submit to save changes.  The changes will overwrite the data in the database
# that can be displayed in the collection page.

def update_collection(request, funkopopname_id):
    editpop = FunkoPopName.objects.get(pk=funkopopname_id)
    form = CollectionForm(request.POST or None, instance=editpop)
    if form.is_valid():
        form.save()
        return redirect('collection')
    return render(request, 'editcollection.html', {'editpop': editpop, 'form': form})

# a function for deleting objects in the database.  A button in the Collection table colored red for each item in the
# database to be able to delete that item.  There is a conformation pop up that will act as a double check to make sure
# you want to delete the item from the database.


def delete_pop(request, funkopopname_id):
    deletepop = FunkoPopName.objects.get(pk=funkopopname_id)
    deletepop.delete()
    return redirect('collection')

# function for a web scrape to pull specific details from a website to be displayed on a django template for the funko
# app

def pop_news(request):
    # URL to be scraped
    url = "https://hotstuff4geeks.com/funko-pop-news/"
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/95.0.4638.54 Safari/537.36",
        "Accept-Language": "en",
    }
    r = requests.get(url, headers=headers)
    # utilizing the BeautifulSoup and lxml modules
    soup = BeautifulSoup(r.text, "lxml")
    popnews = soup.find_all('article')

    pop_list = []

    for news in popnews:
        names_pop = news.find(class_='elementor-post__title').get_text()
        date_pop = news.find(class_='elementor-post-date')
        info_pop = news.a['href']

        info = {
            "title": names_pop.strip(),
            "date": date_pop,
            "link": info_pop
        }
        pop_list.append(info)

    return render(request, 'popnews.html', {'pop_list': pop_list})




