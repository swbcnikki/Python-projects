import json

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import comment
import requests
import http.client

from .models import BirdDescription
from .forms import BirdDescriptionForm
from django.http import HttpResponseRedirect


# Create your views here.

# View to display home page.

def florida_birds_home(request):
    # render method takes the request object and template name as arguments
    # returns httpResponse object with rendered text.
    return render(request, 'FloridaBirds/FloridaBirds_home.html')


# View to add a bird to database.


def add_bird(request):
    # declare variable called "form".
    form = BirdDescriptionForm(data=request.POST or None)
    if form.is_valid():  # method is used to validate all fields in the user form.
        form.save()
        return redirect('florida_birds_add_bird')  # go back to "add bird url"
    else:
        print(form.errors)
        form = BirdDescriptionForm()
        context = {'form': form}  # dictionary item
    return render(request, 'FloridaBirds/FloridaBirds_add_bird.html', context)


# View to display all birds from database.

def display_all_birds(request):
    bird_data = BirdDescription.objects.all()
    return render(request, "FloridaBirds/FloridaBirds_display_all_birds.html", {'bird_data': bird_data})


# View to display detail of one bird from the display_all_birds file.

def display_details(request, pk):
    birddetail = BirdDescription.objects.get(pk=pk)
    return render(request, "FloridaBirds/FloridaBirds_details.html", {"birddetail": birddetail})


# View to search for a particular bird using the search box


# def search_collection(request):
# if request.method == "POST":
# searched = request.POST['searched']
# birds = BirdDescription.objects.filter(Q(name__contains=searched))

# return render(request, 'FloridaBirds/FloridaBirds_search_collection.html',
# {'searched': searched, 'birds': birds})
# else:
# return render(request, 'FloridaBirds/FloridaBirds_search_collection.html', {})


def edit(request, pk):
    birdedit = BirdDescription.objects.get(pk=pk)
    form = BirdDescriptionForm(request.POST or None, instance=birdedit)
    if form.is_valid():
        form.save()
        return redirect('florida_birds_display_all_birds')

    return render(request, "FloridaBirds/FloridaBirds_edit.html", {"birdedit": birdedit, 'form': form})


def delete(request, pk):
    birddelete = BirdDescription.objects.get(pk=pk)
    if request.method == 'POST':
        birddelete.delete()
        return redirect('florida_birds_display_all_birds')
    context = {'birddelete': birddelete}
    return render(request, 'FloridaBirds/FloridaBirds_delete.html', context)


def api(request):
    conn = http.client.HTTPSConnection("public-holiday.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "public-holiday.p.rapidapi.com",
        'x-rapidapi-key': "9afece8438msh5f25fff510a60bbp1954d2jsn7f98f53b6d37"
    }

    conn.request("GET", "/2021/US", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    return render(request, 'FloridaBirds/FloridaBirds_api.html')
