from django.shortcuts import render, get_object_or_404, redirect
from .models import EFTItems
from .forms import EFTForm
import requests


# Create your views here.
def eft_home(request):
    return render(request, 'EFT_Items/EFT_Items_home.html')


def eft_create_record(request):
    form = EFTForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eft_all_items')
    else:
        print(form.errors)
        form = EFTForm()
    context = {
        'form': form,
    }
    return render(request, 'EFT_Items/EFT_Items_create.html', context)


def eft_all_items(request):
    # Gets all objects from the database sorted by name
    sorted_items = EFTItems.objects.order_by('name')
    return render(request, 'EFT_Items/EFT_Items_display_items.html', {'items': sorted_items})


def eft_details(request, pk):
    details = get_object_or_404(EFTItems, pk=pk)
    context = {
        'details': details,
    }
    return render(request, 'EFT_Items/EFT_Items_details.html', context)


def eft_edit(request, pk):
    items = EFTItems.objects.get(pk=pk)
    form = EFTForm(request.POST or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('eft_all_items')
    context = {
        'items': items, 'form': form
    }
    return render(request, 'EFT_Items/EFT_Items_edit.html', context)


def eft_delete(request, pk):
    item = EFTItems.objects.get(pk=pk)
    item.delete()
    return redirect('eft_all_items')


def eft_api(request):
    def run_query(query):
        response = requests.post('https://tarkov-tools.com/graphql', json={'query': query})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

    mutant = """
    {
        itemsByName(name: "mutant") {
            name
            shortName
        }
    }
    """

    result = run_query(mutant)
    filtered = result['data']['itemsByName']
    name = filtered[0]['name']
    shortname = filtered[0]['shortName']
    print(name)
    print(shortname)
    return render(request, 'EFT_Items/EFT_Items_api.html')
