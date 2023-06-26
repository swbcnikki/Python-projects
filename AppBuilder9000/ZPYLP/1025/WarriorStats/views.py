from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlayerForm
from .models import Player


def stats_Home(request):
    return render(request, 'WarriorStats/stats_Home.html')


def add_player(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('add_player')
    content = {'form': form}
    return render(request, 'WarriorStats/create.html', content)


def view_player(request):
    players = Player.Players.only('Name')
    return render(request, 'WarriorStats/players.html', {'players': players})


def view_details(request, pk):
    players = get_object_or_404(Player, pk=pk)
    return render(request, 'WarriorStats/details.html', {'players': players})

