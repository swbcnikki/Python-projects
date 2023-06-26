from django.shortcuts import render, redirect, get_object_or_404
from .forms import PokemonForm
from .models import Pokemon
from django.contrib import messages

# imports needed to run BeautifulSoup and do web scraping
import requests
from bs4 import BeautifulSoup

# All of these functions here will need to be added to the urls.py files to be able to make them work and to call them

# this is just so we can go back to the home page when you click home on the navbar
def pokeDexHome(request):
    return render(request, 'PokeDex/PokeDex_home.html')

# here we are making it so that we are getting the info from the PokemonForm and saving the info to the database
# if the request.method == post and the form info is valid and then redirecting to the home page for now
def addPokemon(request):
    form = PokemonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_pokemon')
    content = { 'form': form }
    return render(request, 'PokeDex/AddPokemon_form.html', content)

# this is how we are going to get the info from our models.py and then have that info returned and displayed onto
# hour showPokemon.html file
def show_pokemon(request):
    show_pokemon = Pokemon.object.all()

    context = {'show_pokemon': show_pokemon}
    return render(request, 'PokeDex/PokeDex_showPokemon.html', context)

# this is how we end up getting the primary key from our DB and use it to get and show the details when the pokemon name is selected
def pokemon_details(request, pk):
    details = get_object_or_404(Pokemon, pk=pk)
    context = {'details': details}
    return render(request, 'PokeDex/pokemonDetails.html', context)

""" here we are getting our pokemon form from our model and making sure that the new info the user put in is valid within
our form requirement fields and if it is to save the new info they put in and then redirect back to the show pokemon html"""
def edit_pokemon(request, pk):
    show_pokemon = get_object_or_404(Pokemon, pk=pk)
    form = PokemonForm(data=request.POST or None, instance=show_pokemon) # this instance makes it show the info that was already entered in about the pokemon you are editing
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_pokemon')
    context = {'form': form}
    return render(request, 'PokeDex/PokeDex_edit.html', context)

# This is our function we set up to pass into our delete html for if the user wants to delete a pokemon from their pokedex and if they
# click no it wil then redirect back to their pokedex and if they click yes then a pop up will confirm they want to do that and then redirect to the pokedex
def delete_pokemon(request, pk):
    show_pokemon = get_object_or_404(Pokemon, pk=pk)
    form = PokemonForm(data=request.POST or None, instance=show_pokemon)
    if request.method == 'POST':
            show_pokemon.delete()
            return redirect('show_pokemon')
    return render(request, 'PokeDex/PokeDex_delete.html', {'show_pokemon': show_pokemon, 'form': form})

"""
======================================================
    BEAUTIFUL SOUP SECTION
========================================================================
"""

""" here we have our code to scrape the number and name of the pokemon from the pokemon.com website to put into our
search page later. We use the request.get here and put in the web link we are wanting to scrape the info from and then do
the beautifulSoup below and pass in the page content and have it sent back through html.parser and then we make 2 empty
lists that we will use further down to get the final info we want later. We then do a for loop to find all the 'li' tags
in the web link above and then wek ask to get the text from those and to strip them to a string and then we say if the 
length of the text is what we want to return the info and we append the info below and then we make a var to get the info
we want and pass in an example of what we want returned and then we do a while loop to get our final output and we get 
that by putting the name and number of the pokemon we get from our pokemon list into a var and then we append the var
and add 1 each time we run the while loop until we get to the final number and each time it runs it will get the pokemon
name and number assosiated with it and give it back to us and then we pass the final list into our context and have it
returned with our search.html page and then we will run the list in the search.html page to display the info we got from 
here."""
def pokeDex_search(request):
    page = requests.get("https://www.pokemon.com/us/pokedex/")
    soup = BeautifulSoup(page.content, 'html.parser')
    pokemon_list = []
    final_list = []
    for i in soup.find_all('li'):
        li_text = i.get_text(strip=True)
        if len(li_text):
            pokemon_list.append(li_text)
    d = pokemon_list.index('1 - Bulbasaur')
    i = 0
    while i < 898: # number of pokemon
        poke_list = pokemon_list[d + i]
        final_list.append(poke_list)
        i += 1
    context = {'final_list': final_list}
    return render(request, 'PokeDex/PokeDex_search.html', context)

"""
==================================================================================
    API SECTION 
=========================================================================================================
"""

def more_info(request):
    complete_info = []
    if request.method == "POST": # we run this if else statement to make sure that the user input isn't blank
        value = request.POST['pokemon'].lower()
        if value == "":
            messages.info(request, 'Please enter in a Pokémon name!') # if it is blank run this message
        else: # else run the code below
            info = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(value)) # this is the api key with our value var
            poke_info = info.json() # this is to get the api info in json
            poke_name = poke_info # we then put that info above into a new var to reference below
            poke_abilities = poke_name['abilities'] # this is to go into the abilities section of the api
            poke_type = poke_name['types'] # we do the same thing with type
            poke_picture = poke_name['sprites'] # here is how we get the picture location of the pokemon
            front_picture = poke_picture['front_default'] # this is to get the front default picture of pokemon

            pokemon_type = ""
            ''' here we are doing a for loop so we can get all the types of what the pokemon might be. We make a var and
            have it assigned to a blank str and then in the for loop we use the poke_type var because it goes into the 
            api and finds the section that has Types in it and then we will loop through all the values inside that section
            of the api and find the sections inside it of Type and then inside type we find the section with Name to get
            the actual name of the types the pokemon are. So if they have 1 or more type, this loop will get any info that
            is associated there with the specific pokemon called.'''
            for pokemon in poke_type:
                pokemon_type = pokemon_type + pokemon['type']['name'] + ", "

            # here we are doing the same thing as above but to get the abilities of the pokemon
            pokemon_ablity = ""

            for poke in poke_abilities:
                pokemon_ablity = pokemon_ablity + poke['ability']['name'] + ", "
            # this is then going to be a var holding our dictionary that is holding the values of the info we got from
            # the above code.
            results = {
                'value': value, # this is the value of the poke name the user put or copied into our search bar in html
                'species': pokemon_type, # this is the value of the poke types we got from our for loop above
                'ability': pokemon_ablity, # this is the value of the poke abilites we got from the for loop above
                'front_picture': front_picture # this is value of our front_picture var above
            }
            complete_info.append(results) # we then take that info and pass it into our empty list var from the very top
            # and then append the parameter passed in to this to get the string and then use the new info stored inside
            # complete_info and create a for loop in our html to get the info out of it and to be displayed on our api html page.

            # here is the new schema we made to take in the api info from above and put those values into our original schema values
            # and are able to save the pokemon info from the api into our pokedex(database)
            new_pokemon = Pokemon.object.create(
                name = value,
                type = pokemon_type,
                abilities = pokemon_ablity

            )
            new_pokemon.save()

        context = {'complete_info': complete_info}
        return render(request, 'PokeDex/PokeDex_api.html', context) # this is how we return this info to our api.html page and make dictionaries out of the info we got
                        # and then we turn them into vars in the html when we call them to display the info we got here
    else:
        return render(request, 'PokeDex/PokeDex_api.html')




