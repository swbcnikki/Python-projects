from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipesForm
from .models import Recipes
from bs4 import BeautifulSoup
import requests


def recipes_home(request):
    return render(request, 'Recipes/recipeshome.html')


def recipes_create(request):
    form = RecipesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('recipes_home')
    context = {
        'form': form,
    }
    return render(request, 'Recipes/recipescreate.html', context)


def recipes_display(request):
    recipes_list = Recipes.Recipe.all()
    context = {
        'recipes_list': recipes_list
    }
    return render(request, 'Recipes/recipesdisplay.html', context)


def recipes_details(request, pk):
    details = get_object_or_404(Recipes, pk=pk)
    context = {'details': details}
    return render(request, 'Recipes/recipesdetails.html', context)


def recipes_edit(request, pk):
    item = get_object_or_404(Recipes, pk=pk)
    form = RecipesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('recipes_display')
    context = {'form': form}
    return render(request, 'Recipes/recipesedit.html', context)


def recipe_delete(request, pk):
    item = get_object_or_404(Recipes, pk=pk)
    form = RecipesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('recipes_display')
    return render(request, 'Recipes/recipesdelete.html', {'item': item, 'form': form})


def recipes_edit(request, pk):
    item = get_object_or_404(Recipes, pk=pk)
    form = RecipesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('recipes_display')
    context = {'form': form}
    return render(request, 'Recipes/recipesedit.html', context)


def recipes_delete(request, pk):
    item = get_object_or_404(Recipes, pk=pk)
    form = RecipesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('recipes_display')
    return render(request, 'Recipes/recipesdelete.html', {'item': item, 'form': form})


# utilizes BeautifulSoup to extract the HTML containing the steps of a recipe from any
# hard-coded allrecipes.com page - prints to the console and renders the HOME page
# Called by clicking the "Import" nav item
def recipes_import(request):
    page = requests.get('https://www.allrecipes.com/recipe/8144/mardi-gras-king-cake/')
    soup = BeautifulSoup(page.content, 'html.parser')

    # get the name of the recipe
    title_text = soup.find("h1", {"class": "headline heading-content elementFont__display"})
    title = title_text.text.strip()

    # get the description of the recipe
    description_section = soup.find("div", {"class": "recipe-summary elementFont__dek--paragraphWithin elementFont__dek--linkWithin"})
    description_text = description_section.find("p")
    description = description_text.text.strip()

    # get the ingredients of the recipe
    ingredients_section = soup.find("ul", {"class": "ingredients-section"})
    ingredients_text = ingredients_section.find_all("span", {"class": "ingredients-item-name elementFont__body"})
    ingredients = ''
    for i in ingredients_text:
        ingredients += i.text.strip() + ", "

    # get the instructions
    instructions_section = soup.find("ul", {"class": "instructions-section"})
    instructions_text = instructions_section.find_all("div", {"class": "paragraph"})
    instructions = ''
    for i in instructions_text:
        instructions += i.text.strip() + " "

    recipe = [title, description, ingredients, instructions]
    context = {'recipe': recipe}

    return render(request, 'Recipes/recipesimport.html', context)
