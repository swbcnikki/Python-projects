from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import StockForm
from .models import StockData


def stock_home_page(request):
    return render(request, 'StockTracker/StockTrackerHome.html')


def stock_add_page(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'StockTracker/StockAddPage.html')
    else:
        form = StockForm()

    return render(request, 'StockTracker/StockAddPage.html', {'form': form})


def stock_display_database_page(request):
    stock_list = StockData.objects.all()
    return render(request, 'StockTracker/StockDisplayDatabase.html', {'stock_list': stock_list})


def stock_details(request, pk):
    indiv_stock = get_object_or_404(StockData, pk=pk)
    return render(request, 'StockTracker/StockDetailsPage.html', {'indiv_stock': indiv_stock})

