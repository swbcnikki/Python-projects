from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe
import requests
from .forms import APIForm
import json
# Create your views here.
def Recipes_Home(request):
    return render(request, 'Recipes_Home.html')

def Recipes_Create(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Recipes_Create')
    else:
        print(form.errors)
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'Recipes_Create.html', context)

def Recipes_See(request):
    recipes = Recipe.objects.all()
    return render(request, 'Recipes_See.html', {'recipes': recipes})

def Recipes_Details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('Recipes_See')
        else:
            print(form.errors)
    else:
        return render(request, 'Recipes_Details.html', {'form': form})


def Recipes_Edit(request, pk):
    item = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Recipes_See')
    context = {'form': form}
    return render(request, 'Recipes_Edit.html', context)

def Recipes_Delete(request, pk):
    item = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('Recipes_See')
    context = {'item': item, 'form': form}
    return render(request, 'Recipes_Delete.html', context)

def Recipes_SearchAPI(request):
    form = APIForm(data=request.POST or None) #Calling APIForm in forms.py to get user input
    context = {'response': None, 'apidata': None, 'form': form} #this will be the data that user will send to 'Recipes_API.html'
    if request.method == 'POST': #Checking to see if we got input or not ("did someone press the enter key")
        if form.is_valid(): #Django will parse through the input and determine if it's good or not and will format into cleaned_data
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search" #API website
            querystring = {"query": form.cleaned_data["query"]} #Data being passed to the API
            headers = { #This is what tells the API that I am Me
                'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                'x-rapidapi-key': "712c1c2476msh2252ea9dcf93640p1cccbcjsn0d5ce80ec9d8"
                }
            response = requests.request("GET", url, headers=headers, params=querystring) #Taking all the data and submitting to API to get a response
            apidata = json.loads(response.text)
            context['response'] = response.text #Takes that response and puts it in a format that "Recipes_API can see
            context['apidata'] = apidata

    return render(request, 'Recipes_API.html', context) #Rendering "Recipes_API" and adds the variables and context

