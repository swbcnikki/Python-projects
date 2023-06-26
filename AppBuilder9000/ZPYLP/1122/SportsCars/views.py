from django.shortcuts import render, redirect, get_object_or_404
from .models import SportsCar
from .forms import SportsCarForm


def SportsCars_Home(request):
    return render(request, 'SportsCars_Home.html')


def AddNewCar(request):
    form = SportsCarForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SportsCars_Home')
    content = {'form': form}
    return render(request, 'AddSportsCar.html', content)


def Supercars(request):
    sportscar = SportsCar.objects.all()
    content = {'sportscar': sportscar}
    return render(request, 'Supercars.html', content)


def CarDetails(request, pk):
    cardetails = get_object_or_404(SportsCar, pk=pk)
    content = {'cardetails': cardetails}
    return render(request, 'CarDetails.html', content)
