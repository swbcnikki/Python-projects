from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehiclesForm
from .models import Vehicles



def vehiclesHome(request):
    return render(request, 'vehicles/Vehicles_home.html')

def addVehicles(request):
    form = VehiclesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Vehicles_view')
    content = { 'form': form }
    return render(request, 'vehicles/Vehicles_add.html', content)

def vehicles_view(request):
    vehicles_list = Vehicles.object.all()
    context = {'vehicles_list': vehicles_list}
    return render(request, 'vehicles/Vehicles_view.html', context)

def vehicle_details(request, pk):
    details = get_object_or_404(Vehicles, pk=pk)
    context = {'details': details}
    return render(request, 'vehicles/Vehicles_details.html', context)


