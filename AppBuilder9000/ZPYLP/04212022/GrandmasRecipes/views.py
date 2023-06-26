from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipesForm
from .models import Recipes


def grandmas_home(request):
    return render(request, 'GrandmasRecipes/GrandmasRecipes_home.html')


def grandmas_create(request):
    form = RecipesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('GrandmasRecipes_home')
    content = {'form': form}
    return render(request, 'GrandmasRecipes/GrandmasRecipes_create.html', content)


def grandmas_cookbook(request):
    # recipe = Database name: Recipes, model manager: Recipe get all
    recipes = Recipes.Recipes.all()
    context = {'recipes': recipes}

    return render(request, 'GrandmasRecipes/GrandmasRecipes_cookbook.html', context)


# render GrandmasRecipes_details page, display any recipe in the database
def grandmas_details(request, pk):
    details = get_object_or_404(Recipes, pk=int(pk))  # recipe we want to modify
    content = {'details': details}
    return render(request, 'GrandmasRecipes/GrandmasRecipes_details.html', content)


# render GrandmasRecipes_edit page, save changes to database
def grandmas_edit(request, pk):
    item = get_object_or_404(Recipes, pk=int(pk))  # recipe we want to modify
    form = RecipesForm(data=request.POST or None, instance=item)  # create form and put data in it.

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('GrandmasRecipes_cookbook')  # return to database list
        else:
            print(form.errors)
    content = {'form': form}
    return render(request, 'GrandmasRecipes/GrandmasRecipes_edit.html', content)


# Delete Function
def grandma_delete(request, pk):
    item = get_object_or_404(Recipes, pk=int(pk))  # the recipe we want to delete
    form = RecipesForm(data=request.POST or None, instance=item)  # create form and put data in it.
    if request.method == 'POST':
        item.delete()
        return redirect('GrandmasRecipes_cookbook')  # return to database list
    content = {
        'item': item,
        'form': form,
    }
    return render(request, 'GrandmasRecipes/GrandmasRecipes_delete.html', content)

