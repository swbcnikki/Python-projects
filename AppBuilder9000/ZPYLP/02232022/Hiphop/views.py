import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Choice
from .forms import ChooseForm
from . import Hiphop


def hiphop_home(request):
    # this will return user to hip hop home page
    return render(request, 'Hiphop/hiphop_home.html')

def create_choose(request):
    form = ChooseForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('hiphop_home')
    context = {'form': form}
    return render(request, 'Hiphop/hiphop_create.html', context)

def all_items(request):
    all_hiphop = Choice.objects.all()
    context = {'all_hiphop': all_hiphop}
    return render(request, 'Hiphop/all_items.html', context)

def hiphop_details(request, pk):
    hiphop_request = get_object_or_404(Choice, pk=pk)
    context = {'hiphop_request': hiphop_request}
    return render(request, 'Hiphop/details.html', context)


#def choose_view(request):
 #   choose = choose.objects.all()
  #  return render(request, 'hiphop_view.html', {'choose': choose})