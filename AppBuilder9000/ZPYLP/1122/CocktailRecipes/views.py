from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cocktail, Review
from .forms import CocktailForm, ReviewForm


# view function to render the cocktail recipes home page
def cocktail_recipes_home(request):
    # renders the homepage and passes active to the navbar
    return render(request, 'CocktailRecipes/cocktail_recipes_home.html', {'home_page': 'active'})


# view function to take user input and add new cocktail recipes to the database
def add_cocktail(request):
    form = CocktailForm(data=request.POST or None)
    # checks if the request method came from submitting the add cocktail form on this page
    # or from a link elsewhere in the app
    if request.method == 'POST':
        # validate the form against model parameters
        if form.is_valid():
            form.save()
            # render the updated cocktail list page with new cocktail
            return cocktail_list(request)
    # if the request wasn't the POST method from the add cocktail form
    # render add_cocktail.html page, also create the dictionary content and
    # give it key value pair 'form': variable that contains CocktailForm, and
    # passes navbar active
    content = {'form': form, 'add_cocktail': 'active'}
    return render(request, 'CocktailRecipes/cocktail_recipes_add_cocktail.html', content)


def cocktail_list(request):
    # variable to store all entries to cocktail database ordered by cocktail name
    cocktails = Cocktail.Cocktails.all().order_by('cocktail_name')
    # dictionary storing cocktail variable from above and navbar active page info
    content = {'cocktails': cocktails, 'cocktail_list': 'active'}
    # render cocktail_list.html page, pass it content dictionary from above
    return render(request, 'CocktailRecipes/cocktail_recipes_cocktail_list.html', content)


def cocktail_details(request, pk):
    # variable to store the object with primary key that matches the pk from request or error message
    details = Cocktail.Cocktails.filter(pk=pk).values()[0]
    # empty list to hold non blank ingredient strings
    ingredient_lst = []
    # for loop iterating through selected cocktail object dictionary
    for (key, value) in details.items():
        # this if statement checks the length of the key values,
        # which is used as a filter for the ingredient fields because
        # all ingredient field names are 12 characters long
        # it also checks that there is a value associated with those fields
        if len(key) == 12 and len(value) > 0:
            # if both are true, it appends the value which is a string
            # to the ingredient list
            ingredient_lst.append(value)

    # dictionary to hold variables and values from above
    content = {'details': details, 'ingredient_lst': ingredient_lst}
    # render details.html page, pass it content dictionary form above
    return render(request, 'CocktailRecipes/cocktail_recipes_details.html', content)
