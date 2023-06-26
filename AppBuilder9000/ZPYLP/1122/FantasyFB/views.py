from django.shortcuts import render, redirect, get_object_or_404
from .models import Player
from .forms import NewPlayer
# Create your views here.


def fantasyFB_home(request):
    return render(request, 'fantasyFB_home.html')


def fantasyFB_form(request):
    form = NewPlayer(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fantasyFB_form')
    else:
        print(form.errors)
        form = NewPlayer()
    context = {
        'form': form,
    }
    return render(request, 'fantasyFB_form.html', context)


def fantasyFB_roster(request):
    players = Player.Players.all()
    return render(request, 'fantasyFB_roster.html', {'players': players})


def fantasyFB_details(request, pk):
    players = get_object_or_404(Player, pk=pk)
    return render(request, 'fantasyFB_details.html', {'players': players})
