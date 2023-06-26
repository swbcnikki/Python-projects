from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import MovieForm
from .models import Movies
import requests
from bs4 import BeautifulSoup
import json
from django.contrib import messages

# This renders the homepage of the Movie Reviews App.
def homepage(request):
    return render(request, 'MovieReviews/moviereviews_home.html')

# This adds new Movie Reviews to the database.
def moviereviews_create(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('moviereviews_home')

    context = {
        'form': form
    }
    return render(request, 'MovieReviews/moviereviews_create.html', context)

# This displays movies in the database
def moviereviews_display(request):
    movies = Movies.Movies.all()
    context = {
        'movies': movies
    }
    return render(request, 'MovieReviews/moviereviews_display.html', context)

# This shows the details of the movies in the database.
def moviereviews_details(request, pk):
    movie_item = get_object_or_404(Movies, pk=pk)
    context = {'movie_item': movie_item
    }
    return render(request, 'MovieReviews/moviereviews_details.html', context)

# This allows the user to edit a specific movie in the database
def moviereviews_edit(request, pk):
     movie_item = get_object_or_404(Movies, pk=pk)
     form = MovieForm(data=request.POST or None, instance=movie_item)
     if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('moviereviews_display')
        else:
            print(form.errors)
     else:
        return render(request, 'MovieReviews/moviereviews_edit.html', {'form': form, 'movie_item': movie_item})

# This allows the user to delete an item in the database
def moviereviews_delete(request, pk):
    movie_item = get_object_or_404(Movies, pk=pk)
    if request.method == 'POST':
        movie_item.delete()
        return redirect('moviereviews_display')
    context = {'movie_item': movie_item}
    return render(request, 'MovieReviews/moviereviews_delete.html', context)

# This uses Beautiful Soup to scrape movie data from a website
def moviereviews_scraping(request):
    movie_list = []
    rating_list = []
    page = requests.get("https://www.imdb.com/list/ls024149810/")
    soup = BeautifulSoup(page.content, 'html.parser')
    movie = soup.find('div', class_='sub-list')
    title = movie.find_all('h3', class_='lister-item-header')
    for i in title:
        name = i.find('a')
        movie_title = name.text
        movie_list.append(movie_title)
    movie_ratings = movie.find_all('div', class_='ipl-rating-widget')
    for b in movie_ratings:
        stars = b.find('span', class_='ipl-rating-star__rating')
        rating = stars.text
        rating_list.append(rating)
    print(rating_list)
    print(movie_list)
    movie_info = zip(movie_list, rating_list)
    context = {'movie_info': movie_info}
    return render(request, 'MovieReviews/moviereviews_scraping.html', context)


# This allows the user to search a movie by title and display results using API
def moviereviews_api(request):
    title_list = []
    year_list = []

    if request.method == 'POST':
        userinput = request.POST['userinput']
        if 'userinput' == '':
            messages.info(request, 'Please put in info')
        else:

            url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
            querystring = {"type": "get-movies-by-title", "title": userinput}
            headers = {
                    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
                    'x-rapidapi-key': "25eef8ba99msh15727dc40c123aep11ab94jsn4d74c8cd384d"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            movie = json.loads(response.text)
            movie_results = movie['movie_results']
            if request.method == 'POST':
                for movies in movie_results:
                    titles = movies['title']
                    title_list.append(titles)
                    year = movies['year']
                    year_list.append(year)
            print(title_list)
            print(year_list)
            context = {'title_list': title_list, 'year_list': year_list}

            return render(request, 'MovieReviews/moviereviews_api.html', context)
    else:
        return render(request, 'MovieReviews/moviereviews_api.html')


















