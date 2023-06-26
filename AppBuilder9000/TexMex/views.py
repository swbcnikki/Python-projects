from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import FoodForm
from .models import Food


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def texmex_home(request):
    return render(request, 'TexMex/texmex_home.html')
# Create your views here.

def recipe_page(request):
    foods = Food.objects.all()
    return render(request, 'TexMex/recipe_page.html', {'foods': foods})

def view_recipes(request):
    foods = Food.objects.all()
    return render(request, 'TexMex/texmex_display.html', {'foods': foods})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    return render(request, 'TexMex/present_food.html', {'item': item})

def edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    form = FoodForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('recipe_page')
        else:
            print(form.errors)
    else:
        return render(request, 'TexMex/texmex_edit.html', {'form': form, 'item': item})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('recipe_page')
    content = {"item": item}
    return render(request, "TexMex/confirmDelete.html", content)

def confirmed(request):
    if request.method == 'POST':
        #creates form instance and binds data to it
        form = FoodForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('recipe_page')
    else:
        return redirect('recipe_page')

def createRecord(request):
    form = FoodForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_recipes')
    else:
        print(form.errors)
        form = FoodForm()
    context = {
        'form': form,
    }
    return render(request, "TexMex/createRecord.html", context)
