from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
import requests
import json
from bs4 import BeautifulSoup


# Create your views here.
def eb_home(request):
    return render(request, 'EmpireBuilder/eb_home.html')

def eb_admin_console(request):
    EmpireBuilder = Booking.objects.all()
    return render(request, 'EmpireBuilder/eb_reservation.html', {'EmpireBuilder': EmpireBuilder})
def eb_cancel(request, pk):
    pk = int(pk)
    item = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        item.cancel()
        return redirect('eb_reservation')
    context = {'item': item}
    return render(request, 'eb_home', context)

def eb_reserve(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eb_created')
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, 'EmpireBuilder/eb_reservation.html', context)

def eb_stations(request):
    return render(request, 'EmpireBuilder/eb_stations.html')

def eb_accommodations(request):
    return render(request, 'EmpireBuilder/eb_accommodations.html')

def eb_gallery(request):
    return render(request, 'EmpireBuilder/eb_gallery.html')

def eb_created(request):
    booking = Booking.objects.all()
    content = {'booking': booking}
    return render(request, 'EmpireBuilder/eb_created.html', content)


def eb_details(request, pk):
    rider = get_object_or_404(Booking, pk=pk)
    content = {'rider': rider}
    return render(request, 'EmpireBuilder/eb_details.html', content)

def eb_clear(request):
    package = Booking.objects.all()
    package.delete()
    return render(request, 'EmpireBuilder/eb_reservation.html')

def eb_edit(request, pk):
    rider = get_object_or_404(Booking, pk=pk)
    form = BookingForm(data=request.POST or None, instance=rider)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../created')
    content = {'form': form, 'rider': rider}
    return render(request, 'EmpireBuilder/eb_edit.html', content)

def eb_delete(request, pk):
    rider = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        rider.delete()
        return redirect('../../created')
    content = {'rider': rider}
    return render(request, 'EmpireBuilder/eb_delete.html', content)

#def eb_api(request): #This has not worked yet. 403 error code

#    url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"

#    querystring = {"city": "Seattle", "state": "WA"}

#    headers = {
#        "X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com",
#        "X-RapidAPI-Key": "fa8d801427msh4c0f67b3762da4fp12385bjsn12dc828fb42c"
#    }

#    response = requests.request("GET", url, headers=headers, params=querystring)

#    content = {'response.text': response.text}
#    return render(request, 'EmpireBuilder/eb_api.html', content)

