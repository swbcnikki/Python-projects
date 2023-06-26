from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from .forms import form_addObject
from .models import celestialObjects
import requests
from django.urls import path


# Create your views here.
from django.http import HttpResponse


def StarWatch_home(request):
    return render(request, 'StarWatch/StarWatch_home.html')


def add_object(request):
    form = form_addObject(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('StarWatch_listObjects')
    content = {'form': form}
    return render(request, 'StarWatch/StarWatch_addObject.html', content)


def list_objects(request):
    object_list = celestialObjects.object.all()
    context = {'object_list': object_list}
    return render(request, 'StarWatch/StarWatch_listObjects.html', context)


def object_details(request, pk):
    details = get_object_or_404(celestialObjects, pk=pk)
    context = {'details': details}
    return render(request, 'StarWatch/StarWatch_objectDetails.html', context)


def list_planets(request):
    planets = celestialObjects.object.all().filter(object_type='Planet')
    context = {'planets': planets}
    return render(request, 'StarWatch/StarWatch_filterPlanets.html', context)


def list_stars(request):
    stars = celestialObjects.object.all().filter(object_type='Star')
    context = {'stars': stars}
    return render(request, 'StarWatch/StarWatch_filterStars.html', context)


def list_moons(request):
    moons = celestialObjects.object.all().filter(object_type='Moon')
    context = {'moons': moons}
    return render(request, 'StarWatch/StarWatch_filterMoons.html', context)


def list_other(request):
    others = celestialObjects.object.all().filter(object_type='Other')
    context = {'others': others}
    return render(request, 'StarWatch/StarWatch_filterOther.html', context)


def edit_object(request, pk):
    details = get_object_or_404(celestialObjects, pk=pk)
    form = form_addObject(request.POST or None, instance=details)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('StarWatch_listObjects')
    context = {'form': form}
    return render(request, 'StarWatch/StarWatch_editObject.html', context)

def delete_object(request, pk):
    details = get_object_or_404(celestialObjects, pk=pk)
    if request.method == 'POST':
        details.delete()
        return redirect('StarWatch_listObjects')
    context = {"details": details,}
    return render(request,  'StarWatch/StarWatch_deleteObject.html', context)




