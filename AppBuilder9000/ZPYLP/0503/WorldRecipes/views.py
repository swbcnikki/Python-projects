from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe


def home(request):
    return render(request, 'WorldRecipes/WR_home.html')


def create_recipes(request):
    form = RecipeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('WR_create_recipes')
    context = {'form': form}
    return render(request, 'WorldRecipes/WR_create_recipes.html', context)


def view_recipes(request):
    all_recipes = Recipe.objects.all()
    context = {'all_recipes': all_recipes}
    return render(request, 'WorldRecipes/WR_view_recipes.html', context)


def recipe_details(request, id):
    item = get_object_or_404(Recipe, id=id)
    context = {'item': item}
    return render(request, 'WorldRecipes/WR_recipe_details.html', context)




