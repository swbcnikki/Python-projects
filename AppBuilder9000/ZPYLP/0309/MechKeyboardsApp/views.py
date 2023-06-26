from django.shortcuts import render, get_object_or_404, redirect
from .models import KeyboardList
from .forms import KeyboardListForm
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from bs4 import BeautifulSoup
import requests


# home page render function
def home(request):
    return render(request, 'MechKeyboardsApp/Mech_Keyboards_home.html')


# create record function for the model
def create_record(request):
    form = KeyboardListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Mech_Keyboards_home')
    context = {'form': form}
    return render(request, 'MechKeyboardsApp/Mech_Keyboards_create.html', context)


def keyboard_index(request):
    # Retrieves all objects in templates
    build_list = KeyboardList.objects.order_by(Lower('username').asc())
    paginator = Paginator(build_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'MechKeyboardsApp/Mech_Keyboards_index.html', {'page_obj': page_obj})


def search_results(request):
    name = request.GET.get('user_query')
    if name == '':
        return redirect('keyboard_index')
    else:
        results = KeyboardList.objects.filter(username__iexact=name)
    paginator = Paginator(results, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'MechKeyboardsApp/Mech_Keyboards_search.html', {'page_obj': page_obj})


def build_details(request, pk):
    pk = int(pk)
    build = get_object_or_404(KeyboardList, pk=pk)
    return render(request, 'MechKeyboardsApp/Mech_Keyboards_details.html', {'build': build})


def edit_build(request, pk):
    pk = int(pk)
    build = get_object_or_404(KeyboardList, pk=pk)
    form = KeyboardListForm(data=request.POST or None, instance=build)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('../build_details/')
        else:
            print(form.errors)
    else:
        return render(request, 'MechKeyboardsApp/Mech_Keyboards_edit.html', {'build': build, 'form': form})


def delete_build(request, pk):
    pk = int(pk)
    build = get_object_or_404(KeyboardList, pk=pk)
    if request.method == 'POST':
        build.delete()
        return redirect('keyboard_index')
    return render(request, "MechKeyboardsApp/Mech_Keyboards_delete.html", {"build": build})


def confirm_delete(request):
    if request.method == 'POST':
        form = KeyboardListForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('keyboard_index')
    else:
        return redirect('keyboard_index')


def vendor_spotlight(request):
    # grabs the document from which we will scrape
    page = requests.get("https://kbdfans.com/collections/group-buy")
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all(class_="grid-product__content")
    context_list = []
    # iterates through the list grabbing the specified contents of each element
    for item in items:
        # Product title scraped from document
        title = item.find(class_="grid-product__title").get_text()

        # Product price scraped from document
        price = item.find(class_="grid-product__price").get_text().strip()

        # Scraped image link from the attribute 'data-bgset' within the div with
        # class "grid__image-ratio" in the document.
        img_div = item.find(class_="grid__image-ratio").get('data-bgset')
        attr_split = img_div.split(',')
        img_link = attr_split[4].strip()

        # Scraped product link from document to be used as a hyperlink on the product image
        link = item.find('a').get('href')
        abs_link = ('https://kbdfans.com/' + link)

        item_dict = {
            "title": title,
            "price": price,
            "img_link": img_link,
            "abs_link": abs_link,
        }
        context_list.append(item_dict)

    context = {"context_list": context_list}
    return render(request, 'MechKeyboardsApp/Mech_Keyboards_spotlight.html', context)
