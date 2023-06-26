from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateForm
from .models import Turtles


def turtles_home(request):
    return render(request, 'Turtles/turtles_home.html')


"""
=============================================================
        CRUD SECTION - MODEL: TURTLES
=============================================================
"""


def turtles_create(request):
    form = CreateForm(data=request.POST or None)
    # If POST request, process form data.
    if request.method == 'POST':
        # Checks whether it is valid.
        if form.is_valid():
            form.save()
            return redirect('turtles_home')
    content = {'form': form}
    return render(request, 'Turtles/turtles_create.html', content)


# This function displays all data from the database
def turtles_display(request):
    item = Turtles.Turtles.all()
    context = {'item': item}

    return render(request, 'Turtles/turtles_display.html', context)


# Query database for all data for the primary key, from the 'Turtles' class.
def turtles_details(request, pk):
    details = get_object_or_404(Turtles, pk=pk)
    context = {'details': details}

    return render(request, 'Turtles/turtles_details.html', context)


# Function to edit selected entries from the database, and save the edited data.
def turtles_edit(request, pk):
    item = get_object_or_404(Turtles, pk=pk)
    form = CreateForm(data=request.POST or None, instance=item)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('turtles_display')
    context = {'form': form}
    return render(request, 'Turtles/turtles_edit.html', context)


# Function to delete selected entries from the database. Also makes sure you want to delete entry.
def turtles_delete(request, pk):
    item = get_object_or_404(Turtles, pk=pk)
    form = CreateForm(data=request.POST or None, instance=item)
    if request.method == "POST":
        item.delete()
        return redirect('turtles_display')
    return render(request, 'Turtles/turtles_delete.html', {'item': item, 'form': form})
