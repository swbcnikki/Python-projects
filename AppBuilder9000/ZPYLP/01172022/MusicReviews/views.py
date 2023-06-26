from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ReviewForm
from .models import Review
from bs4 import BeautifulSoup
import requests
import os
import json


# Create your views here.


def music_reviews_home(request):
    # this will return you to the home page of music reviews
    return render(request, 'musicreviews_home.html')


def beautiful_soup(request):
    page = requests.get("https://en.wikipedia.org/wiki/Music")
    soup = BeautifulSoup(page.content, 'html.parser')
    music = soup.find_all('p')
    text = music[1].get_text()
    context = {
        'text': text,
    }
    return render(request, 'musicreviews_beautifulsoup.html', context)


def apiLoad(request):
    url = "https://google-search3.p.rapidapi.com/api/v1/news/q=music+spotify"
    headers = {
        'x-user-agent': "desktop",
        'x-proxy-location': "US",
        'x-rapidapi-host': "google-search3.p.rapidapi.com",
        'x-rapidapi-key': "9afece8438msh5f25fff510a60bbp1954d2jsn7f98f53b6d37",

    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    title = data['entries'][0]
    text = title['title']
    link = title['link']
    published = title['published']
    publishedby = title['source']['title']
    title1 = data['entries'][1]
    text1 = title1['title']
    link1 = title1['link']
    published1 = title1['published']
    publishedby1 = title1['source']['title']
    title2 = data['entries'][2]
    text2 = title2['title']
    link2 = title2['link']
    published2 = title2['published']
    publishedby2 = title2['source']['title']
    context = {
        'text': text,
        'link': link,
        'published': published,
        'publishedby': publishedby,
        'text1': text1,
        'link1': link1,
        'published1': published1,
        'publishedby1': publishedby1,
        'text2': text2,
        'link2': link2,
        'published2': published2,
        'publishedby2': publishedby2,
    }
    print(str(title))
    print(str(response))
    return render(request, 'musicreviews_apiView.html', context)


def createReview(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('review_view')
    else:
        print(form.errors)
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'musicreviews_create.html', context)


def editReview(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('review_view')
    return render(request, 'musicreviews_edit.html', {'item': item, 'form': form})


def review_view(request):
    reviews = Review.objects.all()
    return render(request, 'musicreviews_view.html', {'reviews': reviews})


def back_home(request):
    return render(request, '../templates/home/index.html')


def display_reviews(request, pk):
    item = get_object_or_404(Review, pk=pk)
    return render(request, 'musicreviews_viewlist.html', {'item': item})


def delete(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('review_view')
    context = {"item": item, "form": form}
    return render(request, "musicreviews_confirmDelete.html", context)


def confirmDelete(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('review_view')
    else:
        return redirect('review_view')