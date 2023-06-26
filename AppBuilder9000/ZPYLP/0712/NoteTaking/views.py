from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Categorie
from .forms import NoteForm, CategoryForm
import requests


def Home(request):
    notes = Note.object.all()
    return render(request, 'NoteTaking/NoteTaking_home.html', { 'notes': notes })

def Details(request, pk):
    pk = int(pk)
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(data=request.POST or None, instance=note)

    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('NoteTaking_home')
        else:
            print(form.errors)
    else:
        return render(request, 'NoteTaking/NoteTaking_details.html', { 'form': form })

def AddNotes(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('NoteTaking_home')
    else:
        print(form.errors)
        form = NoteForm()

    context = {
        'form': form
    }

    return render(request, 'NoteTaking/NoteTaking_addnotes.html', context)

def DeleteNotes(request, pk):
    pk = int(pk)
    item = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('NoteTaking_home')

    context = { "item": item }
    return render(request, 'NoteTaking/NoteTaking_confirmdelete.html', context)

def SuggestionsAPI(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('NoteTaking_home')
    else:
        api_call = requests.get("https://www.boredapi.com/api/activity/")
        response = api_call.json()


        # Store type of suggestion in category variable.
        category = response['type'].capitalize()
        category_query = Categorie.object.filter(Name=category)

        ## Check if category already exist.
        ## If not, we will add the category.
        if len(category_query) == 0:
            Categorie(Name=category).save()

        form2 = NoteForm(initial={"Title": response['activity'], "Category": category_query[0].pk})
        context = {
            'title': response['activity'],
            'category': category,
            'form': form2
        }

        return render(request, 'NoteTaking/NoteTaking_suggestions.html', context)

def AddCategories(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('NoteTaking_home')
    else:
        print(form.errors)
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'NoteTaking/NoteTaking_addcategories.html', context)
