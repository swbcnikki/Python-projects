from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocationForm
from django.db import models
from .forms import LocationForm
from .models import Location
from django.http import Http404


def TrackApp_home(request):
    return render(request,"TrackApp\TrackApp_home.html")

def TrackApp_Add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TrackApp_Add')
    else:
        form = LocationForm(request.POST)
        return render(request, 'TrackApp/TrackApp_Add.html',
                      {'form': form})

def TrackApp_display(request):
    location_list = Location.objects.all()
    context = {'location_list': location_list}
    print(location_list)
    return render(request, "TrackApp/TrackApp_display.html", context)

def TrackApp_detail(request,_id):
    try:
        data = Location.objects.get(id =_id)
    except Location.DoesNotExist:
        raise Http404('Data does not exist')

    return render(request,'TrackApp/TrackApp_detail.html',{'data':data})


































