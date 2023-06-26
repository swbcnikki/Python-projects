from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Item, Vendor
from .forms import ItemForm, VendorForm

# Create your views here.
def cim_home(request):
    return render(request, 'cim_home.html')


def cim_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    content = {'item': item}
    return render(request, 'cim_item.html', content)


def cim_list(request):
    try:
        produce = Item.objects.filter(item_category='Produce')
        page = request.GET.get('page')
        paginator = Paginator(produce, 10)
        total_produce = paginator.get_page(page)
    except Exception:
        raise Http404('No items found')

    try:
        other = Item.objects.filter(item_category='Other')
        page = request.GET.get('page')
        paginator = Paginator(other, 10)
        total_other = paginator.get_page(page)
    except Exception:
        raise Http404('No items found')

    content = {'produce': total_produce, 'other': total_other}
    return render(request, 'cim_list.html', content)


""" Working on a fix for this...
def cim_list(request):
    content = {'items': None, 'query': None}
    if 'results' in request.GET and request.GET['results']:
        search = request.GET.get('search', 1)
        results = request.GET['results']

        items = Item.objects.filter(item_category=results)
        paginator = Paginator(items, 10)
        total_items = paginator.page(items)
        content = {'items': total_items, 'query': results}
        return render(request, 'cim_list.html', content)
    else:
        try:
            items = Item.objects.all()
        except Exception:
            raise Http404('No items found')
        page = request.GET.get('page')
        paginator = Paginator(items, 10)
        total_items = paginator.get_page(page)
        content = {'items': total_items, 'query': None}

    return render(request, 'cim_list.html', content)
"""


def cim_listVendor(request):
    try:
        vendors = Vendor.objects.all()
    except Exception:
        raise Http404('No items found')

    page = request.GET.get('page')
    paginator = Paginator(vendors, 10)
    total_vendors = paginator.get_page(page)
    content = {'vendors': total_vendors}
    return render(request, 'cim_listVendor.html', content)


def cim_new(request):
    form = ItemForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            return redirect('cim_list')
    content = {'form': form}
    return render(request, 'cim_new.html', content)


def cim_newVendor(request):
    form = VendorForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cim_home')
    content = {'form': form}
    return render(request, 'cim_newVendor.html', content)



def cim_edit(request):
    form = Item(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['id']
            form.save()
            return cim_item(request, pk)
    return render(request, 'cim_edit.html')



def cim_editVendor(request):
    form = Vendor(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['id']
            form.save()
            return cim_item(request, pk)
    return render(request, 'cim_editVendor.html')

