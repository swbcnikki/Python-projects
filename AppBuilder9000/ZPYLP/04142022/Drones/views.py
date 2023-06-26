from django.http import HttpResponseRedirect
from django.shortcuts import render,  redirect, get_object_or_404
from .forms import DroneForm
from .models import Drone

# Create your views here.


def Drones_home(request):
    return render(request, 'Drones/Drones_home.html', {})


def Drones_create(request):
    form = DroneForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Drones_list')
    context = {'form': form}
    return render(request, 'Drones/Drones_create.html', context)


def Drones_list(request):
    drones_list = Drone.Drones.all()
    context = {'drones_list': drones_list}
    return render(request, 'Drones/Drones_list.html', context)


def Drones_details(request, pk):
    details = get_object_or_404(Drone, pk=pk)
    context = {'details': details}
    return render(request, 'Drones/Drones_details.html', context)






#def select_drone_details(request):
#    select = Drone.Drones.filter(id=1)
#    return render(request, 'Drones/Drones_details.html', {'select': select})


#def select_drone_details(request):
#    select1 = Drone.Drones.get(id__exact=2)
#    return render(request, 'Drones/Drones_details.html', {'select1': select1})


#def select_drone_details(request):
#    select2 = Drone.Drones.get(id__exact=2)
#    return render(request, 'Drones/Drones_details.html', {'select2': select2})


#def select_drone_details(request):
#    select3 = Drone.Drones.get(id__exact=3)
#    return render(request, 'Drones/Drones_details.html', {'select3': select3})

