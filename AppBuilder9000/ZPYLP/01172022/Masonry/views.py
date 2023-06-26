import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import QuoteForm
from .models import Quotes


# Create your views here.
def masonry_home(request):
    # This render function will take the request argument, and return the html document as a response

    return render(request, 'Masonry/Masonry_home.html')


def quote_view(request):
    quotes = Quotes.objects.all()
    return render(request, 'Masonry/quotes_page.html', {'quotes': quotes})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Quotes, pk=pk)
    form = QuoteForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('All_quotes')
        else:
            print(form.errors)
    else:
        return render(request, 'Masonry/Masonry_details.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Quotes, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('masonry_home')
    context = {"item": item}
    return render(request, "Masonry/confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = QuoteForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('masonry_home')
    else:
        return redirect('masonry_home')


def createQuote(request):
    form = QuoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('masonry_home')
    else:
        print(form.errors)
        form = QuoteForm()
    context = {
        'form': form,
    }
    return render(request, 'Masonry/createQuote.html', context)


def gallery(request):
    return render(request, 'Masonry/Masonry_gallery.html')
