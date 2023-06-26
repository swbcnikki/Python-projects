from django.shortcuts import render, get_object_or_404, redirect
from .forms import LocationForm
# pulls in the data from all EuroTrip classes
from .models import Location
import requests
import json


def eurotriphome(request):
    return render(request, 'eurotriphome.html')


def eastern(request):
    return render(request, 'eastern.html')


def easternlocationscreate(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('easternlocationscreate')
    else:
        print(form.errors)
        form = LocationForm()
        context = {
            'form': form,
        }
    return render(request, 'easternlocationscreate.html', context)


def eastern_list(request):
    location_list = Location.objects.all()
    return render(request, 'eastern.html',
            {'location_list': location_list})

# Function to allow user to view a single item


def eurotripdetails(request, pk):
    pk = int(pk)
    item = get_object_or_404(Location, pk=pk)
    return render(request, 'eurotripdetails.html', {'item': item})


def etedit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Location, pk=pk)
    form = LocationForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('eastern')
        else:
            print(form.errors)
    else:
        return render(request, 'etedit.html', {'form': form, 'item':item})


def etdelete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('eastern')
    context = {"item": item}
    return render(request, 'etdelete.html', context)


def currency(request):
    if request.method == 'GET':
        convertfrom = request.GET.get('Currency1')
        convertto = request.GET.get('Currency2')
        amount = request.GET.get('Currency3')
        print(convertfrom, convertto, amount)
        api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want={}&have={}&amount={}'.format(convertto, convertfrom, amount)
        response = requests.get(api_url, headers={'X-Api-Key': 'AjW5PD2G1/MiCDKhJ9RQDw==BNSnGxHcYOKrO3Lk'})
        # render to website importing json module
        if response.status_code == requests.codes.ok:
            print(response.text)
            finalcurrency = response.json()
            return render(request, 'currency.html', {
                'convertfrom': finalcurrency['old_currency'],
                'previousamt': finalcurrency['old_amount'],
                'newcurrency': finalcurrency['new_currency'],
                'finalamount': finalcurrency['new_amount']
            })
        else:
            print("Error:", response.status_code, response.text)
    return render(request, 'currency.html')
