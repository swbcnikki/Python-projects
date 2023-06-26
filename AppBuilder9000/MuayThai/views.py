from django.shortcuts import render, get_object_or_404, redirect
from .forms import FighterForm
from .models import Fighter
import requests
import json
from bs4 import BeautifulSoup



# calls the MuayThai_home home page when requested
def Muay_Thai_Home(request):
    return render(request, 'MuayThai/MuayThai_home.html')


# calls template and accept the form inputs for adding to the db (the create part of it)
def MuayThai_fighter_entry(request):
    form = FighterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MuayThai_display_fighters')
    else:
        print(form.errors)
        form = FighterForm()
    content = {
        'form': form,
    }
    return render(request, 'MuayThai/MuayThai_fighter_entry.html', content)


# Display fighter's names
def MuayThai_display_fighters(request):
    fighters = Fighter.Fighter.all()
    content = {
        'fighters': fighters,
    }
    return render(request, 'MuayThai/MuayThai_display_fighters.html', content)


# call the details template
def MuayThai_fighters_details(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Fighter, pk=pk)
    form = FighterForm(data=request.POST or None, instance=fighter)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('MuayThai_display_fighters')
        else:
            print(form.errors)

    else:
        content = {
            'form': form,
            'fighter': fighter,
        }
        return render(request, 'MuayThai/MuayThai_fighters_details.html', content)


# function to we are deleting from the database
def MuayThai_delete_fighter(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Fighter, pk=pk)
    if request.method == 'POST':
        fighter.delete()
        return redirect('MuayThai_display_fighters')
    content = {
        "fighter": fighter,
    }
    return render(request, "MuayThai/MuayThai_delete.html", content)


# function used to confirm the delete action
def MuayThai_delete(request):
    if request.method == 'POST':
        form = FighterForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('MuayThai_display_fighters')
    else:
        return redirect('MuayThai_display_fighters')



    ######## API code section. Renders into terminal


def MuayThai_fighters_api(request,):
    weight = []
    fighter_rank = []
    fighter_name = []

    ### Code snippet (python requests)
    url = "https://current-ufc-rankings.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Host": "current-ufc-rankings.p.rapidapi.com",
        "X-RapidAPI-Key": "e62380c195msh635581688557802p1f24ebjsnf7d94c60773c"
    }

    response = requests.request("GET", url, headers=headers)
    ### END Code snippet (python requests)

    fight_rankings = json.loads(response.text)  # It returns a Python object.
    for i in fight_rankings:  # 'i' is the variable in fight_rankings
        weight_class = i['weightClass']
        weight.append(weight_class)  # The append() method takes a single item as an input parameter and adds that to the end of the list
        fighters = i['fighters']
        for j in fighters:  # 'j' is the variable in fighters

            rankings = j['fighter_ranking']
            fighter_rank.append(rankings)
            names = j['fullName']
            fighter_name.append(names)

    # prints out variables
    print(weight)
    print(fighter_rank)
    print(fighter_name)


    # Zip lists together to easily display all data
    zipped_list = zip(weight, fighter_rank, fighter_name)
    context = {
        'zipped_list': zipped_list
    }


    return render(request, 'MuayThai/MuayThai_fighters_api.html', context)



    ### BEAUTIFUL SOUP ###
def MuayThai_soup(request):
    muays = []  # Top Muays name list

    page = requests.get("https://fightersvault.com/best-muay-thai-fighters/#:~:text=Samart%20Payakaroon&text=He%20is%20arguably%20the%20best,successful%20in%20his%20early%20career.")
    soup = BeautifulSoup(page.content, 'html.parser')
    rankings = soup.find_all('strong')

    for i in rankings:
        rank = i.text.strip()
        muays.append(rank)
    l = muays[6], muays[7]  # Grabs the elements that need to be joined.
    fix = ' '.join(l)  # Joins the two elements and places them in a variable
    muays.insert(6, fix)  # Inserts joined elements into array at appropriate index
    del muays[8]  # Removes unnecessary element
    del muays[7]  # Removes unnecessary element

    context = {'muays': muays}
    return render(request, 'MuayThai/MuayThai_beautifulSoup.html', context)
