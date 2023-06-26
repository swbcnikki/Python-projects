from django.shortcuts import render, get_object_or_404, redirect
from .models import Ryder
from .forms import RyderForm


def home(request):
    return render(request, "SnowboardingHome.html")

def AddNewRyder(request):
    form = RyderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('AddNewRyder')
    content = {'form': form}
    return render(request, 'New_Ryder.html', content)

def GetAllRyders(request):
    if request.method == 'GET':
        ryders_queryset = Ryder.objects.all() #returns queryset
        ryders_dict = {'ryders': ryders_queryset}
        return render(request, 'Dear_Ryder.html', ryders_dict)
        # get functions must return a dictionary not a queryset

def Ryder_Details(request, pk):
    Ryder_Details = get_object_or_404(Ryder, pk=pk)
    context = {'Ryder_Details': Ryder_Details}
    return render(request, 'Ryder_Details.html', context)

def Edit_Ryder(request, pk):
    ryder = get_object_or_404(Ryder, pk=pk)
    form = RyderForm(data=request.POST or None, instance=ryder)
    if form.is_valid():
        form.save()
        return redirect('Ryders')
    content = {'form': form}
    return render(request, 'Edit_Ryder.html', content)

def Delete_Ryder(request, pk):
    ryder = get_object_or_404(Ryder, pk=pk)
    if request.method == 'POST':
        ryder.delete()
        return redirect('Ryders')
    content = {'ryder': ryder}
    return render(request, 'Delete_Ryder.html', content)











