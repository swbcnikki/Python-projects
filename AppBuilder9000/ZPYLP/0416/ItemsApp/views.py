from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


# Create your views here.
def home(request):
    """Function to open the homepage."""
    return render(request, 'ItemsApp/musicfiles_home.html')


def new_item(request):
    """Creates the form used for user input"""
    form = ItemForm(data=request.POST or None)  # Creates the form from forms.py.
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('select_item')  # When the form is created, redirect to the home page.
    content = {'form': form}  # Dictionary for form data entry.
    return render(request, 'ItemsApp/new_item.html', content)


def display_items(request):
    """Creates a form displaying the current items in the templates."""
    item = Item.objects.all().values()  # Grabs all values from all items in the templates.
    content = {'item': item}  # Dictionary for the items.
    return render(request, 'ItemsApp/display_items.html', content)


def select_item(request):
    """Creates a list of items from the templates with anchor tag to select."""
    item_list = Item.objects.all()  # Grabs all items from all items in the templates.
    content = {'item_list': item_list}
    return render(request, "ItemsApp/get.html", content)


def item_details(request, pk):
    """Displays the chosen item from 'select_item' function."""
    pk = int(pk)
    item_get = Item.objects.filter(pk=pk)
    content = {'item_get': item_get}
    return render(request, "ItemsApp/details_page.html", content)


def edit_page(request):
    """Page that displays a drop-down menu for editing items in the templates."""
    items = Item.objects.all()
    return render(request, 'ItemsApp/edit_page.html', {'items': items})


def edit_form(request, pk):
    """Renders a new page for input and edit form."""
    pk = int(pk)
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('select_item')
        else:
            print(form.errors)
    else:
        return render(request, 'ItemsApp/edit_items.html', {'form': form})


def delete_item(request, pk):
    """Grabs the information from the primary key of the item to delete."""
    pk = int(pk)
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('select_item')
    context = {"item": item}
    return render(request, "ItemsApp/confirm_delete.html", context)


def confirm_delete(request):
    """Creates a page got the user to confirm the deletion of the item from the templates."""
    if request.method == 'POST':
        # Creates form instance and binds data to it
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('select_item')
    else:
        return redirect(home)
