from django.shortcuts import render, redirect, get_object_or_404
import requests, json
from .forms import BookForm, SearchForm, WishlistForm
from BookClubApp.models import Book
from django import template
from bs4 import BeautifulSoup
from django.core.paginator import Paginator



register = template.Library()


# display home page template
def BookClubApp_home(request):
    return render(request, 'BookClubApp/BookClubApp_home.html')


# display about page template
def BookClubApp_about(request):
    return render(request, 'BookClubApp/BookClubApp_about.html')


# display a list of books that the user has read (read=True)
def BookClubApp_booklist(request):
    # will return read book items from templates
    data = Book.objects.filter(read=True)
    # get current page number
    page = request.GET.get('page', 1)
    # set max results to show per page
    paginator = Paginator(data, 3)
    # set paginator attributes
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    books = {
        "books": books
    }
    return render(request, 'BookClubApp/BookClubApp_booklist.html', books)


# display an individual book
def BookClubApp_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'BookClubApp/BookClubApp_book.html', context={'book': book})


# get the value from the search form and display the results from the api
def BookClubApp_explore(request):
    if request.method == 'POST':
        form = SearchForm(data=request.POST or None)

        if form.is_valid():
            # get search term from form
            searchTerm = form.cleaned_data['searchTerm']
            # add search term to google books api url
            api_response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + searchTerm + '&maxResults=18')
            # get json response
            jsonData = api_response.json()['items']

            # create a dictionary for all values
            responseData = {}
            # iterate through response and add them to the dictionary
            for i in range(len(jsonData)):
                # create dictionary for this iteration of the for loop
                indvResponse = {}
                # try blocks are necessary for results to display correctly.
                # Some results do not have all of the fields and will give a
                # KeyError if this is not included.
                # get imagelinks
                try:
                    indvResponse['imageLink'] = jsonData[i]['volumeInfo']['imageLinks']['thumbnail']
                except KeyError:
                    indvResponse['imageLink'] = ''
                # get title
                try:
                    indvResponse['title'] = jsonData[i]['volumeInfo']['title']
                except KeyError:
                    indvResponse['title'] = ''
                # get authors
                try:
                    indvResponse['authors'] = jsonData[i]['volumeInfo']['authors']
                except KeyError:
                    indvResponse['authors'] = ''
                # get description
                try:
                    indvResponse['description'] = jsonData[i]['volumeInfo']['description']
                except KeyError:
                    indvResponse['description'] = ''
                # add field values to the overall response dictionary
                responseData[i] = indvResponse;

            # create a dictionary of the overall response dictionary (responseData),
            # the search term from the search form (searchTerm)
            # and the WishlistForm (form)
            # for display on the BookClubApp_explore.html page
            context = {
                'responseData': responseData,
                'searchTerm': searchTerm,
                'form': WishlistForm(),
            }

        else:
            # if form is not valid, return to the search page
            return redirect('BookClubApp_searchForm')

    return render(request, 'BookClubApp/BookClubApp_explore.html', context)


# display the search form on the search.html page
def BookClubApp_searchForm(request):
    context = {}
    context['form'] = SearchForm()
    return render(request, 'BookClubApp/BookClubApp_search.html', context)


# add new book to the templates
def BookClubApp_AddBook(request):
    form = BookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return to the booklist page after new book added
            return redirect('BookClubApp_bookList')
    content = {'form' : form}
    return render(request, 'BookClubApp/BookClubApp_AddBook.html', content)


# edit book from the templates
def BookClubApp_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('BookClubApp_book', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'BookClubApp/BookClubApp_edit.html', {'form' : form})


# delete book from the templates
def BookClubApp_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # if method is post, then delete the book object
    if request.method == 'POST':
        book.delete()
        # return to booklist page after deleting book
        return redirect('BookClubApp_bookList')
    context = {
        "book" : book
    }
    return render(request, 'BookClubApp/BookClubApp_delete.html', context)


# edit book from the templates
def BookClubApp_MarkRead(request, pk, read):
    book = get_object_or_404(Book, pk=pk, read=read)
    print(book.read)
    if book.read == False:
        book.read = True
        print(book.read)
        book.save()
        context = {
            'book':book
        }
        return redirect('BookClubApp_book', pk=book.pk)
    context = {
        'book': book
    }
    return render(request, 'BookClubApp/BookClubApp_book.html', context)


# add new book to wishlist
def BookClubApp_AddBookWishlist(request):
    form = WishlistForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return to the wishlist page after new book added
            return redirect('BookClubApp_wishlist')
    content = {'form' : form}
    return render(request, 'BookClubApp/BookClubApp_AddBook.html', content)


# display a list of books the user has not read (read=False)
def BookClubApp_wishlist(request):
    # will return book items from templates where read is false
    data = Book.objects.filter(read=False)
    # get current page number
    page = request.GET.get('page', 1)
    # set max results to show per page
    paginator = Paginator(data, 3)
    # set paginator attributes
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    books = {
        "books": books
    }

    return render(request, 'BookClubApp/BookClubApp_wishlist.html', books)


# authors returned from the api can be a list,
# so this method allows you cut characters from the string in the template
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


# Scrap Barnes and Noble top books list page to display the top 20 books in the app
def BookClubApp_scraping(request):
    # get url
    page = requests.get("https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8")
    # parse html with Beautiful Soup
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find list items
    listItems = soup.find_all('li', class_="record")
    # create overall dictionary for response
    returnList = {}
    # iterate through list items
    for i in range(len(listItems)):
        # create dictionary for current list item
        item_response = {}
        # get purchase link
        purchase_link = listItems[i].h3.a['href']
        item_response['formatted_link'] = 'https://www.barnesandnoble.com' + purchase_link
        # get image link
        image = listItems[i].img['src']
        # add https: to image link and add it to the dictionary
        item_response['formatted_image'] = 'https:' + image
        # add title to dictionary
        item_response['title'] = listItems[i].h3.a.text
        # add authors to dictionary
        item_response['authors'] = listItems[i].find('div', class_="product-shelf-author").text

        # add current list item to the overall dictionary
        returnList[i] = item_response

    # create dictionary for display on BookClubApp_toplist.html
    context = {
        'returnList': returnList,
        'form': WishlistForm(),
    }

    return render(request, 'BookClubApp/BookClubApp_toplist.html', context)


# add one to the key value
def add(value):
    newValue = value + 1

    return newValue