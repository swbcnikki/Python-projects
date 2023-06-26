from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def Val_home(request):
    return render(request, 'ValItems/Val_home.html')


def AddItem(request):
    form = ItemForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('AddItem')
    content = {'form': form}
    return render(request, 'ValItems/AddItem.html', content)


def Items(request):
    items = Item.item_object.all()
    return render(request, 'ValItems/Items.html', {'items': items})


def Details(request, pk):
    items = get_object_or_404(Item, pk=pk)
    return render(request, 'ValItems/Details.html', {'items': items})


def Val_edit(request, pk):
    v_edit = get_object_or_404(Item, pk=pk)
    form = ItemForm(data=request.POST or None, instance=v_edit)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Items')
    return render(request, 'ValItems/Val_edit.html', {'form': form})

def Val_delete2(request, pk):
    items_delete = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=items_delete)
    if request.method == 'POST':
        items_delete.delete()
        return redirect('Items')
    return render(request, 'ValItems/Val_delete_true.html', {'items_delete': items_delete})

def Val_delete_true(request):
    if request.method == 'POST':
        form = ItemForm(data=request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('Items')
    else:
        return render(request, 'ValItems/Items.html')
