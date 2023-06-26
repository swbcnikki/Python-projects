from django.shortcuts import render, redirect, get_object_or_404
from .models import PreciousMetalsItem
from .forms import MetalForm
import http.client
import mimetypes
import requests
import json
from bs4 import BeautifulSoup


# Create your views here.

# home html

def home(request):
    return render(request, 'PreciousMetals_home.html', {})


# add inventory

def inventory(request):
    form = MetalForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PreciousMetals_inventory')
    content = {'form': form}
    return render(request, 'PreciousMetals_inventory.html', content)


# query all items in inventory

def list_items(request):
    inv_list = PreciousMetalsItem.metals.all()
    return render(request, 'PreciousMetals_listing.html', {'inv_list': inv_list})


# single item details


def item_details(request, id):
    item_dets = get_object_or_404(PreciousMetalsItem, id=id)
    inv_content = {'item_dets': item_dets}
    return render(request, 'PreciousMetals_details.html', inv_content)


# edit an item


def edit_item(request, id):
    item_dets = get_object_or_404(PreciousMetalsItem, id=id)
    form = MetalForm(request.POST or None, instance=item_dets)
    if form.is_valid():
        form.save()
        return redirect('PreciousMetals_listing')
    content = {'form': form}
    return render(request, 'PreciousMetals_edit.html', content)


# delete item


def delete_item(request, id):
    item_dets = get_object_or_404(PreciousMetalsItem, id=id)
    if request.method == 'POST':
        item_dets.delete()
        return redirect('PreciousMetals_listing')
    delete = {'item_dets': item_dets}
    return render(request, 'PreciousMetals_delete.html', delete)


# api/soup scrapping for rates on metals

def metal_rates(request):
    # connection for gold
    conn = http.client.HTTPSConnection("www.goldapi.io")
    payload = ''
    headers = {
        'x-access-token': 'goldapi-6buwskraz9tg4-io',
        'Content-Type': 'application/json'
    }
    conn.request("GET", "/api/XAU/USD", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    gold_data = data.get('price')
    # connection for silver
    conn1 = http.client.HTTPSConnection("www.goldapi.io")
    conn1.request("GET", "/api/XAG/USD", payload, headers)
    res1 = conn1.getresponse()
    data1 = json.loads(res1.read())
    silver_data = data1.get('price')
    # beatifulsoup Canadian gold 1oz maple leaf scrap
    result = requests.get("https://www.mintstategold.com/canadian-gold-1oz-2021-maple-leaf-bu-18997.html")
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    item = soup.find('div', class_="price-box instock price-final_price")
    get_item = str(item.span.findChild("meta"))
    get_item = get_item.split('"')[1]
    get_item = '$' + get_item
    # return all data
    msg1 = {'silver_data': silver_data, 'gold_data': gold_data, 'get_item': get_item}
    return render(request, 'PreciousMetals_rates.html', msg1)


