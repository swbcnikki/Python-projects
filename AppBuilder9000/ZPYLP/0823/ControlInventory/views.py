from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, ProductForm
from .models import Account, Product



def home(request):
    """Home page render"""
    return render(request, 'ControlInventory/ControlInventory_home.html')

def createuser(request):
    """Creates a form to create a user account"""
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ControlInventory_account.html')
    content = {'form': form}
    return render(request, 'ControlInventory/ControlInventory_account.html', content)

def addproduct(request):
    """Creates a form to allow user input into dB"""
    form = ProductForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ControlInventory_home.html')
    content = {'form': form}
    return render(request, 'ControlInventory/ControlInventory_addproduct.html', content)

def productinfo(request):
    """Creates a page to list all items in the dB"""
    inv_list = Product.objects.all() # Grabs all items from all items in the templates.
    return render(request, 'ControlInventory/ControlInventory_productinfo.html', {'inv_list': inv_list})

def select_item(request):
    """Creates a list of items from the templates with anchor tag to select."""
    item_list = Product.objects.all()  # Grabs all items from all items in the templates.
    content = {'item_list': item_list}
    return render(request, "ControlInventory/ControlInventory_details.html", content)


def item_details(request, pk):
    """Displays the chosen item from 'select_item' function."""
    pk = int(pk)
    item_get = Product.objects.filter(pk=pk)
    content = {'item_get': item_get}
    return render(request, "ControlInventory/ControlInventory_detailspage.html", content)

