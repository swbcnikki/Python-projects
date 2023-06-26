from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe
# import pagination
from django.core.paginator import Paginator
# import requests to access websites
import requests
# importing beautifulsoup
from bs4 import BeautifulSoup


# first instruction on what to do if "home" get invoked
def recipe_home(request):
    # renders in the browser
    return render(request, 'Recipe_Maker/Recipe_Maker_home.html')


# creates a new entry in the templates
def create_recipe(request):
    recipe_form = RecipeForm(request.POST or None)  # gets information from the form

    # if the form is valid
    if recipe_form.is_valid():
        # save information
        recipe_form.save()
        # returns user "home"
        return redirect('Recipe_Maker')
    # if not valid
    else:
        # prints errors
        print(recipe_form.errors)
        # create an empty version of the forms and pass it into a dictionary
        recipe_form = RecipeForm()
    context = {
        'recipe_form': recipe_form,
    }
    # returns the user to the create webpage with the dictionary
    return render(request, 'Recipe_Maker/Recipe_Maker_create.html', context)


# lists out items in the templates
def list_recipes(request):
    # old code to display items in templates
    # recipe_list = Recipe.objects.all()

    # set up Pagination
    p = Paginator(Recipe.objects.all().order_by('recipe_name'), 5)
    page = request.GET.get('page')
    recipes = p.get_page(page)

    return render(request, 'Recipe_Maker/Recipe_Maker_display.html', {'recipes': recipes})


# function to display a detailed view of items
def recipe_details(request, pk):
    # pk is the primary key
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'Recipe_Maker/Recipe_Maker_details.html', {'recipe': recipe})


# function to update recipe in templates
def recipe_update(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    # if a user POSTS use RecipeForm otherwise don't use anything
    form = RecipeForm(request.POST or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect('list_recipes')

    return render(request, 'Recipe_Maker/Recipe_Maker_update.html', {'recipe': recipe, 'form': form})


# function to delete a recipe in the templates
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        recipe.delete()
        return redirect('list_recipes')

    return render(request, 'Recipe_Maker/Recipe_Maker_confirmDelete.html', {'recipe': recipe})


def bsoup(request):
    page = requests.get('https://www.foodnetwork.com/recipes/food-network-kitchen/apple-pie-recipe-2011423')
    # prints out HTML content of a page
    page.content
    # using BeautifulSoup to parse the document
    soup = BeautifulSoup(page.content, 'html.parser')

    # find_all returns a list or you either need to use an index or iterate through the list
    header = soup.find_all('span', class_='o-AssetTitle__a-HeadlineText')[0].get_text()

    # outputs a list of objects with with the span tag and specified class
    ingredients = soup.find_all('span', class_='o-Ingredients__a-Ingredient--CheckboxLabel')
    # empty list to hold strings from the for statement
    list_ingredients = []
    # [1:] skips the first (index of 0) in the ingredients' list
    for i in ingredients[1:]:
        # get_text() strips the tags off the object and returns a string
        text = i.get_text()
        # add the string to list_ingredients
        list_ingredients.append(text)

    # outputs a list of objects with the li tags and the specified class
    description = soup.find_all('li', class_='o-Method__m-Step')
    list_description = []
    for d in description:
        text = d.get_text()
        list_description.append(text)

    context = {
        'header': header,
        'ingredients': list_ingredients,
        'description': list_description,
    }
    return render(request, 'Recipe_Maker/Recipe_Maker_bsoup.html', context)