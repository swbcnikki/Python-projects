from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import PickupForm
from .models import Pickup
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect


# Create your views here.
def basketballHome(request):
    return render(request, 'Basketball/Basketball_home.html')


def pickupGameGet(request):
    posts = Pickup.games.all()
    content = {'posts': posts}
    return render(request, 'Basketball/Basketball_Get.html', content)


def basketballPickup(request):
    # displays page and Pickup model
    form = PickupForm(data=request.POST or None)
    posts = Pickup.games.all()
    # if method is post saves form if valid
    if request.method == 'POST':
        form_valid = form.is_valid()
        if form_valid:
            instance = form.save(commit=False)
            instance.save()
            return redirect("Pickup_Games")
    # else if 'GET' displays the page and the Pickup model
    else:
        content = {'form': form, 'posts': posts}
        return render(request, 'Basketball/Basketball_Pickup.html', content)


def searchPickup(request):
    # if request.method == 'POST':
    #   searched = request.POST['searched']
    #  posts = Pickup.games.filter(name__contains=searched)
    # content = {'searched': searched, 'posts': posts}
    # return render(request, 'Basketball/Basketball_Search.html', content)
    # else:
    # return render(request, 'Basketball/Basketball_Home.html')
    searched = request.POST['searched']
    posts = Pickup.games.filter(name__contains=searched)
    content = {'posts': posts}
    return render(request, 'Basketball/Basketball_Search.html', content)


def basketballDetail(request, pk):
    obj = get_object_or_404(Pickup, id=pk)
    content = {'obj': obj}
    return render(request, 'Basketball/Basketball_Details.html', content)


def basketballEdit(request, pk):
    obj = get_object_or_404(Pickup, id=pk)
    form = PickupForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            game = form.save(commit=False)
            game.save()

    content = {'form': form}
    return render(request, 'Basketball/Basketball_EditAndDelete.html', content)


def basketballDelete(request, pk):
    obj = get_object_or_404(Pickup, id=pk)
    obj.delete()

    return render(request, 'Basketball/Basketball_home.html')
