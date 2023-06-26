from django.shortcuts import render, redirect, get_object_or_404
from .form import StockForm
from .models import WatchStock


def home(request):
    return render(request, 'StockApp/StockApp_home.html')


def base(request):
    return render(request, 'StockApp/StockApp_base.html')


def new(request):
    form = StockForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('StockApp_home')
    content = {'form': form}
    return render(request, 'StockApp/StockApp_newstock.html', content)


def watchlist(request):
    all_stocks = WatchStock.objects.all()
    context = {'all_stocks': all_stocks}
    return render(request, "StockApp/StockApp_Watchlist.html", context)


def details(request, pk):
    this_stock = get_object_or_404(WatchStock, pk=pk)
    all_stocks = {'this_stock': this_stock}
    context = all_stocks
    return render(request, "StockApp/StockApp_Details.html", context)


def confirm(request, pk):
    pk = int(pk)
    this_stock = get_object_or_404(WatchStock, pk=pk)
    context = {"this_stock": this_stock}
    if request.method == 'POST':
        this_stock.delete()
        return redirect("StockApp_Watchlist")
    return render(request, "StockApp/StockApp_confirm.html", context)


def edit(request, pk):
    pk = int(pk)
    this_stock = get_object_or_404(WatchStock, pk=pk)
    form = StockForm(data=request.POST or None, instance=this_stock)
    if request.method == 'POST':
        if form.is_valid():
            save_form(form)
            return redirect('StockApp_Watchlist')
    return render(request, 'StockApp/StockApp_edit.html', {'form': form})


def save_form(form):
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
    else:
        print(form.errors)



