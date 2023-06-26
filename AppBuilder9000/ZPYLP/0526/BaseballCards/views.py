from django.shortcuts import render, redirect, get_object_or_404
from .forms import BaseballCardForm
from .models import BaseballCard


def cards_home(request):
    return render(request, 'BaseballCards/BaseballCards_home.html')


def add_card(request):
    form = BaseballCardForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BaseballCards_home')
    content = {'form': form}
    return render(request, 'BaseballCards/BaseballCards_add.html', content)


def catalog(request):
    cards = BaseballCard.BaseballCards.all()
    content = {'cards': cards}
    return render(request, 'BaseballCards/BaseballCards_catalog.html', content)


def details(request, pk):
    pk = int(pk)
    cards = BaseballCard.BaseballCards.filter(pk=pk)
    context = {'cards': cards}
    return render(request, 'BaseballCards/BaseballCards_details.html', context)



