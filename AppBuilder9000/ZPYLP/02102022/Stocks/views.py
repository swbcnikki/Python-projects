import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Stocks
from .forms import StocksForm
from bs4 import BeautifulSoup

# Create your views here.


def stocks_home(request):
    return render(request, 'Stocks/stocks_home.html')


def favorites(request):
    stocks = Stocks.objects.all()
    return render(request, 'Stocks/stocks_favorites.html', {'stocks': stocks})


def add_favorites(request):
    form = StocksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('stocks_favorites')
    else:
        print(form.errors)
        form = StocksForm()
    context = {
        'form': form,
    }
    return render(request, 'Stocks/stocks_add_favorites.html', context)


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Stocks, pk=pk)
    return render(request, 'Stocks/stocks_details.html', {'item': item})


def edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Stocks, pk=pk)
    form = StocksForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('stocks_favorites')
        else:
            print(form.errors)
    else:
        return render(request, 'Stocks/stocks_edit.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Stocks, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('stocks_favorites')
    else:
        return render(request, "Stocks/confirm_delete.html", {'item': item})


def confirm(request):
    if request.method == 'POST':
        #   creates form instance and binds data to it
        form = StocksForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('stocks_favorites')
    else:
        return redirect('stocks_favorites')


def news(request):
    return render(request, 'Stocks/stocks_news.html')


def stock_news(request):
    feed = []

    page = requests.get("https://www.marketwatch.com/latest-news?mod=top_nav")
    soup = BeautifulSoup(page.content, 'html.parser')

    article = soup.find('div', class_='column column--primary j-moreHeadlineWrapper')
    news_article = article.find_all(class_='article__content')
    #   Retrieves the title, link to article, and summary of article

    for i in news_article:
        title = i.find(class_="article__headline").get_text()
        link = i.a["href"]
        news_array = (title, link)
        feed.append(news_array)

    context = {
        'feed': feed
    }

    return render(request, 'Stocks/stocks_news.html', context)


