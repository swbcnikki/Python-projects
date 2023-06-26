from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import Player

# Displays Home Page



def blazerstats_home(request):
    return render(request, 'BlazerStats/musicfiles_home.html')


def blazerstats_create(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("blazerstats_create")

    return render(request, 'BlazerStats/Blazercreate.html', {"form":form})


def blazerstats_players(request):
    player_list = Player.objects.all()
    return render(request, 'BlazerStats/Players.html', {'player_list': player_list})


def blazerstats_details(request, pk):
    details = Player.objects.get(pk=pk)
    return render(request, 'BlazerStats/details.html', {'details': details})


def player_delete(request, pk):
    item = get_object_or_404(Player, pk=pk)
    form = PlayerForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect("blazerstats_players")
    return render(request, 'BlazerStats/delete.html', {'item': item, 'form': form})

def player_edit(request, pk):
    item = get_object_or_404(Player, pk=pk)
    form = PlayerForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("blazerstats_players")
    content = {'form': form}
    return render(request, 'BlazerStats/edit.html', content)