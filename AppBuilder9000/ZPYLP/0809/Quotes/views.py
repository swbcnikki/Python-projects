from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import QuoteForm
from .models import Quote
# Create your views here.
def home(request):
    return render(request, 'Quotes/Quotes_home.html',)

def Quotes_add(request):
    form = QuoteForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Quotes_add')
    return render(request, 'Quotes/Quotes_add.html', {'form': form})

def Quotes_display(request):
    Quotes_data = Quote.objects.all()
    return render(request, 'Quotes/Quotes_display.html', {'Quotes_data': Quotes_data})

def Quotes_details(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'Quotes/Quotes_details.html', {'quote': quote})

def Quotes_edit(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    form = QuoteForm(request.POST or None, instance=quote)
    if form.is_valid():
        form.save()
        return redirect('Quotes_display')
    return render(request, 'Quotes/Quotes_edit.html', {'form': form})


def Quotes_validate(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        quote.delete()
        return redirect('Quotes_display')
    return render(request, 'Quotes/Quotes_validate.html', {'quote': quote})
