from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SuperCarsForm
from .models import SuperCars



def SuperCarsHome(request):

    return render(request, 'SuperCars/SuperCarsHome.html')

def SuperCarsDetails(request, pk):

    products = get_object_or_404(SuperCars, pk=pk)
    return render(request, 'SuperCars/SuperCarsDetails.html', {'products': products})

def SuperCarsDisplay(request):
    products = SuperCars.objects.all()
    return render(request, 'SuperCars/SuperCarsDisplay.html', {'products': products})

#adding comment

def CreateRecord(request):
    form = SuperCarsForm(data=request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('SuperCars_Home')
        else:
            print(form.errors)
            form = SuperCarsForm()
    context = {
         'form': form,
        }

    return render(request, 'SuperCars/CreateRecord.html', context)
