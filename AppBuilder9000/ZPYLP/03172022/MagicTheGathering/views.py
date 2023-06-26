import json
from json import JSONDecodeError
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Collection, Card
from .forms import CardForm, CollectionForm
from django.contrib import messages
from bs4 import BeautifulSoup



def MagicTheGathering_home(request):
     #collection = Collection.Collection.all()
     #content = {'collection': collection}
     return render(request, 'MagicTheGathering/MagicTheGathering_home.html')


def collection(request):
     cards = Card.Cards.all()
     context = {'cards': cards}
     return render(request, 'MagicTheGathering/ViewCollection.html', context)


def create_collection(request):
     form = CollectionForm(data=request.POST or None)
     if request.method == 'POST':
          if form.is_valid():
               form.save()
               return redirect('create')
     content = {'form': form}
     return  render(request, 'MagicTheGathering/CreateNewCollection.html', content)

def create_card(request):
     form = CardForm(data=request.POST or None)
     if request.method == 'POST':
          if form.is_valid():
               form.save()
     content = {'form': form}
     return render(request, 'MagicTheGathering/AddCardTransaction.html', content)

def details(request, pk):
     card_details = get_object_or_404(Card, pk=pk)
     context = {'card_details':card_details}
     return render(request, 'MagicTheGathering/CardDetails.html', context)


def editCardInfo(request, pk):
    card_details = get_object_or_404(Card, pk=pk)
    form = CardForm(data=request.POST or None, instance=card_details)
    if request.method == 'POST':
         if form.is_valid():
              form.save()
              return redirect('collection')
         else:
              print(form.errors)
    return render(request, 'MagicTheGathering/CardEdit.html', {'form': form})

def delete_card(request, pk):
    item = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('collection')
    context = {"item": item,}
    return render(request, "MagicTheGathering/Magic_confirmdelete.html", context)

def MagicTheGathering_API(request):
    url = "https://api.magicthegathering.io/v1/cards"

    if request.method == "POST":
        value = request.POST['mtg'].capitalize()
        if value == "":
            messages.info(request, "Please enter a card name")
        paramaters = {
            'name': value
        }
        response = requests.get(url, params=paramaters)
        try:
            response.raise_for_status()
            jsonResponse= response.json()
        except (requests.HTTPError, JSONDecodeError):
            errorMessage = 'Please enter a valid card'
        else:
            if jsonResponse['cards']:
                data = json.loads(response.text)
                card_info= data['cards']
                cards=card_info[0]
                name= cards['name']
                type= cards['type']
                color= cards['colors']
                manaCost=cards['manaCost']
                text= cards['text']
                print(name)
                content = {'name':name, 'type':type, 'color':color, 'manaCost':manaCost, 'text':text }
                return render(request, "MagicTheGathering/Magic_API.html", content)
            else:
                return render(request, "MagicTheGathering/Magic_API.html")
    else:
        return render(request, "MagicTheGathering/Magic_API.html")


def How_Too(request):
    if request.method == 'POST':
        page = requests.get("https://en.wikipedia.org/wiki/Magic:_The_Gathering")
        soup = BeautifulSoup(page.content, 'html.parser')
        refined = soup.find_all('div', class_='vector-body')
        for t in refined:
            defa = t.find_all('p')
            ptag1 = defa[1]
            ptagt1 = ptag1.text
            ptag2= defa[2]
            ptagt2 = ptag2.text
            defa = t.find_all('p')
            ptag3 = defa[3]
            ptagt3 = ptag3.text
            ptag4= defa[4]
            ptagt4 = ptag4.text
            ptag5 = defa[5]
            ptagt5 = ptag5.text
            ptag6 = defa[6]
            ptagt6 = ptag6.text
            ptag7 = defa[7]
            ptagt7 = ptag7.text
            about1 = ptagt1
            about2 = ptagt2
            about3 = ptagt3
            about4 = ptagt4
            about5 = ptagt5
            about6 = ptagt6
            about7 = ptagt7
        print(about1, about2, about3, about4, about5, about6, about7)
        context = {'about1':about1, 'about2':about2, 'about3':about3, 'about4':about4, 'about'
                   'about5':about5, 'about6':about6, 'about7':about7}
        return render(request, "MagicTheGathering/About.html", context)
    else:
        return render(request, 'MagicTheGathering/About.html')




