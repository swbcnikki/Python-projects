from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import KnifeForm
from .forms import SearchForm
from .models import ChefKnives
import json


# Create your views here.

def home(request):
    return render(request, 'ChefKnives/ChefKnives_Home.html')


def chefknives_view(request):
    view = ChefKnives.objects.all()
    return render(request, 'ChefKnives/ChefKnives_View.html', {'view': view})


# create a function
def chefknives_create(request):
    # create object of form
    form = KnifeForm(data=request.POST or None)
    # check if form data is valid
    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect('ChefKnives_Create')
        else:
            print(form.errors)
            form = KnifeForm()
    context = {'form': form}
    return render(request, 'ChefKnives/ChefKnives_Create.html', context)


def chefknives_details(request, pk):
    details = get_object_or_404(ChefKnives, pk=pk)
    context = {'details': details}
    return render(request, "ChefKnives/ChefKnives_Details.html", context)


def chefknives_edit(request, pk):
    obj = get_object_or_404(ChefKnives, pk=pk)
    form = KnifeForm(data=request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ChefKnives_View')
    else:
        return render(request, "ChefKnives/ChefKnives_Edit.html", {'form': form})


def chefknives_delete(request, pk):
    obj = get_object_or_404(ChefKnives, pk=pk)
    form = KnifeForm(data=request.POST or None, instance=obj)
    if request.method == 'POST':
        obj.delete()
        return redirect('ChefKnives_View')
    context = {
        "object": obj
    }
    return render(request, "ChefKnives/ChefKnives_Delete.html", context)


def chefknives_soup(request):
    knives = []  # knife name list

    page = requests.get("https://www.cnet.com/home/kitchen-and-household/best-chef-knife-for-2022/")
    soup = BeautifulSoup(page.content,
                         'html.parser')  # create an instance of the BeautifulSoup class to parse our document
    knives_soup = soup.find('div', class_='col-7 article-main-body row')
    knife = knives_soup.find_all('div', class_='shortcode listicle')

    for i in knife:  # iterate through knife through each div tag
        knifes = i.find('p')  # find all p tags as knife name
        chef = knifes.text.strip()  # strip tags
        knives.append(chef)  # append chef to knives list

    print(knives)  # output to console

    context = {'knives': knives}
    return render(request, 'ChefKnives/ChefKnives_Soup.html', context)


def chefknives_api(request):
    list = []
    price = []
    stars = []
    url = "https://free-amazon-data-scraper.p.rapidapi.com/search/Chef%20Knives"

    querystring = {"api_key": "0fd5b0c1fffb09a1c70c1db4f0afe341"}

    headers = {
        "X-RapidAPI-Host": "free-amazon-data-scraper.p.rapidapi.com",
        "X-RapidAPI-Key": "143604b401mshd765f5d870ec324p1e3404jsn76662d978015"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    item_results = json.loads(response.text)

    test = item_results['ads']

    for item in test:
        x = item['name']
        list.append(x)

        y = item['price']
        price.append(y)

        z = item['stars']
        stars.append(z)

    print(list)
    print(price)
    print(stars)

    reviews = zip(list, price, stars)
    context = {'reviews': reviews}
    return render(request, 'ChefKnives/ChefKnives_Api.html', context)


# def chefknives_search(request):
#     result = {}
#     x = request.cleaned_data['x']
#     url = "https://free-amazon-data-scraper.p.rapidapi.com/search/Chef%20Knives"
#
#     querystring = {"api_key": "0fd5b0c1fffb09a1c70c1db4f0afe341"}
#
#     headers = {
#         "X-RapidAPI-Host": "free-amazon-data-scraper.p.rapidapi.com",
#         "X-RapidAPI-Key": "143604b401mshd765f5d870ec324p1e3404jsn76662d978015"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     if response.status_code == 200:  # SUCCESS
#         result = response.json()
#         result['success'] = True
#     else:
#         result['success'] = False
#         if response.status_code == 404:  # NOT FOUND
#             result['message'] = 'No entry found for "%s"' % x
#         else:
#             result['message'] = 'The Amazon API is not available at the moment. Please try again later.'
#
#     return render(request, 'ChefKnives/ChefKnives_Api.html')

