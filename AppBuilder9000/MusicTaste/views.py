from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import User
import requests
import json
from bs4 import BeautifulSoup


def musictaste_home(request):
    return render(request, "MusicTaste/MusicTaste_home.html")


def test(request):
    return render(request, "MusicTaste/test.html")


def registerform(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MusicTaste_home')
    context = {'form': form}
    return render(request, 'MusicTaste/test.html', context)


def userdetails(request, pk):
    details = get_object_or_404(User, pk=pk)
    context = {'details': details}
    return render(request, 'MusicTaste/MusicTaste_details.html', context)


def displayusers(request):
    display = User.Users.all()
    context = {'display': display}
    return render(request, 'MusicTaste/MusicTaste_display.html', context)

