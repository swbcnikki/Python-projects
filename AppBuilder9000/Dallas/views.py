from django.shortcuts import render, redirect, get_object_or_404
from .forms import DallasForm
from .models import Dallas

def home(request):
    return render(request, 'Dallas/Dallas_home.html')

def raffle(request):
    form = DallasForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../list')
    context = {'form': form}
    return render(request, 'Dallas/Dallas_raffle.html', context)

def DisplayRaffle(request):
    raffle_list = Dallas.Dallas.all()
    context = {'Dallas': raffle_list}
    return render(request, 'Dallas/Dallas_list.html', context)

def RaffleDetails(request, pk):
    item = get_object_or_404(Dallas, pk=pk)
    context = {'item': item}
    return render(request, 'Dallas/Dallas_details.html', context)
