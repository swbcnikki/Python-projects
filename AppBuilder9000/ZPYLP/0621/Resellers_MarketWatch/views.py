from django.http import Http404
from django.shortcuts import render, redirect
from .forms import WebscrapeForm, UserLoginForm
from .models import WebScrape
# Create your views here.


def home(request):
    form = UserLoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Account')

    context = {
        'form': form
    }
    return render(request, 'Resellers_MarketWatch/MarketWatch_home.html', context)


def account(request):
    form = WebscrapeForm(data=request.POST or None)
    if request.method == 'POST':
        print('Method is POST')
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('Listview')

    context = {
        'form': form
    }
    return render(request, 'Resellers_MarketWatch/AccountPage.html', context)


def all_webscrape(request):
    dataset = WebScrape.WebScrape_db.all()
    context = {
        'dataset': dataset
    }
    return render(request, 'Resellers_MarketWatch/Listview.html', context)


def detailsview(request, pk):
    try:
        data = WebScrape.WebScrape_db.get(id=pk)
    except WebScrape.DoesNotExist:
        raise Http404('Data does not exist')

    return render(request, 'Resellers_MarketWatch/DetailView.html', {'data': data})