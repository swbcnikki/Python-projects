from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.contrib import messages

from .forms import ComposerForm
from .models import Composer
import requests
from bs4 import BeautifulSoup
import json


# Create your views here.
def composers(request):
    return render(request, 'Composers/composers_home.html')


def create_composer(request):
    form = ComposerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('composers_home')
    content = {'form': form}
    return render(request, 'Composers/composers_create.html', content)


def composers_list(request):
    composer_list = Composer.Composers.all()
    context = {'composer_list': composer_list}
    return render(request, 'Composers/composers_list.html', context)


def composers_details(request, pk):
    details = get_object_or_404(Composer, pk=pk)
    context = {'details': details}
    return render(request, 'Composers/composers_details.html', context)


def composers_edit(request, pk):
    item = get_object_or_404(Composer, pk=pk)
    form = ComposerForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('composers_list')
    context = {'form': form}
    return render(request, 'Composers/composers_edit.html', context)


def composers_delete(request, pk):
    item = get_object_or_404(Composer, pk=pk)
    form = ComposerForm(request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('composers_list')
    return render(request, 'Composers/composers_delete.html', {'item': item, 'form': form})


"""List of the top 25 composers according to this site"""
'''def composer_scraping2(request):
    top20composers=[]
    page = requests.get('https://www.thetoptens.com/greatest-classical-composers/')
    soup = BeautifulSoup(page.content, 'html.parser')
    composers_soup = soup.find_all('b')
    for i in composers_soup:
        if i != 'hublink':
            composers = i.text
            top20composers.append(composers)
            print(composers)
    return render(request, 'Composers/top100_composers.html')'''


def composer_scraping(request):
    top100composers = []
    page = requests.get('https://digitaldreamdoor.com/pages/best-classic-comp.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    composers_soup = soup.find('div', class_='list')
    composer = composers_soup.find_all('span')
    for i in composer:
        names = i.text
        top100composers.append(names)
    print(top100composers)
    context = {'top100composers': top100composers}
    return render(request, 'Composers/top100_composers.html', context)


'''Adding a source to a api fpr, 21st Century Composers that gets name and birth'''


'''
def composer_search(request):
    composers_fname = {}
    if 'complete_name' in request.GET:
        complete_name=request.GET('complete_name')
        URL='https://api.openopus.org/composer/list/search/{complete_name}.json' """"% will be replaced with composer name to search"""
        response = requests.get(URL)
        composers_fname=response.json()
        return render (request, 'Composers/composers_api.html', {'composers_fname':composers_fname})

def composers_api(request):
    URL = 'https://api.openopus.org/composer/list/epoch/21st Century.json'
    response = requests.request('GET', URL)
    composer_name = json.loads(response.text)
    for composers in composer_name['composers']:
        complete_name = composers["complete_name"]
        composer_birth = composers["birth"]
        composer_group=complete_name, composer_birth
        print(composer_group)
    return render(request, 'Composers/composers_api.html')'''


'''def composer_search(request):
    composers_fname = []
    if request.method == 'POST':
        value = request.POST['complete_name'].lower()
        URL='https://api.openopus.org/composer/list/search' + str(value) + '.json'
        if value=="":
            messages.info(request, 'Please enter a composers name')
        else:
            response=requests.get(URL)
            print(response.status_code)
            composers_name = response.json()
            names = composers_name['composers']
            composers_fname.append(names)
            print(composers_fname)
        return render(request, 'Composers/composers_api.html',{'composers_fname':composers_fname})
    else:
        return render(request, 'Composers/composers_api.html')'''

'''Try #3 using a new API, the Oxford Dictionary, to get words that people do not understand'''

def oxford_api(request):
    app_id=	'7fcc67f3'
    app_key='4789fb95bb5e7ca65c438b8d8e1630af'
    language='en-us'
    fields = 'definitions'
    strictMatch = 'false'
    whole_definition=[]
    if request.method=='POST':
        value=request.POST['word_id'].lower()
        if value=="":
            messages.info(request, 'Please enter a search term')
        else:
            url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + value + '?fields=' + fields + '&strictMatch=' + strictMatch;
            info=requests.get(url,headers={'app_id':app_id, 'app_key':app_key})
            oxford_info=info.json()
            result=oxford_info['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
            whole_definition.append(result)
        context={'value':value,'whole_definition':whole_definition}
        return render(request, 'Composers/composers_api.html', context)
    else:
        return render(request, 'Composers/composers_api.html')
