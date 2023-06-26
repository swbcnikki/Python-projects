from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddBookForm
from .models import AddBook, FavoriteBook
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from django.contrib import messages


# render home page
def books_home(request):
    return render(request, 'Books/Books_Home.html')


# function to render built in form from my model AddBook
def books_add_book(request):
    form = AddBookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('books_reviews')
    content = {'form': form}
    return render(request, 'Books/Books_AddBook.html', content)


# function to fetch all objects created from form and render
def books_reviews(request):
    book_entries = AddBook.objects.all()
    content = {'book_entries': book_entries}
    return render(request, 'Books/Books_Reviews.html', content)


# function to get all attributes of object and render on details page
def books_details(request, pk):
    details = get_object_or_404(AddBook, pk=pk)
    context = {'details': details}
    return render(request, 'Books/Books_Details.html', context)


# function to delete AddBook object
def books_delete(request, pk):
    delete_book = AddBook.objects.get(pk=pk)
    if request.method == 'POST':
        delete_book.delete()
        return redirect('books_reviews')
    return render(request, 'Books/Books_Delete.html')


# function to update AddBook form, instance argument fills fields with selected element.
def books_update(request, pk):
    update_books = AddBook.objects.get(pk=pk)
    form = AddBookForm(request.POST or None, instance=update_books)
    if form.is_valid():
        form.save()
        return redirect('books_reviews')
    return render(request, 'Books/Books_Update.html',
                  {'update_books': update_books,
                   'form': form})


"""Utilizing API from rapidAPI to find book reviews from 'BookShelves API'. Very important to make variables into empty
list first and then append variables from for loop into those same lists. Also consolidate all lists in zip variable
and pass that into context, then use for loop with each list as the iterator in your template file."""


def books_api(request):
    title = []
    author = []
    rating = []
    description = []

    url = "https://bookshelves.p.rapidapi.com/books"

    headers = {
        "X-RapidAPI-Host": "bookshelves.p.rapidapi.com",
        "X-RapidAPI-Key": "1aed881129msh0e4e702933d3b57p1d0a71jsnaba2c0d6b2f8"
    }

    response = requests.request("GET", url, headers=headers)
    books_info = json.loads(response.text)
    for items in books_info['Books']:
        book_title = items['title']
        title.append(book_title)

        book_author = items['author']
        author.append(book_author)

        book_rating = items['review']
        rating.append(book_rating)

        book_description = items['description']
        description.append(book_description)


    zipped_list = zip(title, author, rating, description)

    context = {
            'zipped_list': zipped_list,
        }
    return render(request, 'Books/Books_API.html', context)


""" This function will pull from the same API as above but will show only the titles of each book inside of a list, allowing the
    user to select from an individual book and then giving the user an option to add it to the database."""


def books_fav(request):
    book_titles = []
    url = "https://bookshelves.p.rapidapi.com/books"

    headers = {
        "X-RapidAPI-Host": "bookshelves.p.rapidapi.com",
        "X-RapidAPI-Key": "1aed881129msh0e4e702933d3b57p1d0a71jsnaba2c0d6b2f8"
    }

    response = requests.request("GET", url, headers=headers)
    books_info = json.loads(response.text)
    book_information = books_info['Books']
    for i in book_information:
        book_name = i['title']
        book_titles.append(book_name)
    if request.method == 'POST':
        value = request.POST['value']
        for fields in book_information:
            the_titles = fields['title']
            if value == the_titles:
                new_books = FavoriteBook.Favorite_Book.create(Title=fields['title'],
                                             Author=fields['author'],
                                             Rating=fields['review'],
                                             )
                new_books.save()
        return redirect('view_fav_books')
    else:
        return render(request, 'Books/Books_Fav.html', {'book_titles': book_titles})


"""Function to view books added to the database from the API data"""


def view_fav_books(request):
    added_favorites = FavoriteBook.Favorite_Book.all()
    context = {'added_favorites': added_favorites}
    return render(request, 'Books/Books_ViewFav.html', context)
