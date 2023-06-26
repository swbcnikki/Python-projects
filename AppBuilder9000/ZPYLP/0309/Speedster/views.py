from django.shortcuts import render, get_object_or_404
from .forms import VehicleForm
from .models import Vehicle


# Home page function
def Speedster_home(request):
    form = VehicleForm(data=request.POST or None)
    content = {'form': form}
    return render(request, 'Speedster/speedster_home.html', content)

def Speedster_add(request):
    form = VehicleForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'Speedster/speedster_home.html')
    content = {'form': form}
    return render(request,'Speedster/speedster_add.html', content)



def Speedster_profile(request):
    return render(request,'Speedster/speedster_profile.html',)

def Speedster_database(request):
    cars = Vehicle.Vehicle.all()
    context = {'cars': cars}
    return render(request, 'Speedster/speedster_database.html', context)

def Speedster_details(request, id):
    context = {
        'cars': get_object_or_404(Vehicle, id=id)
    }
    return render(request,'Speedster/speedster_details.html', context)

def Speedster_index(request):
    cars = Vehicle.Vehicle.objects.all()
    context = {'cars': cars}
    return render(request,'Speedster/speedster_index.html', context )