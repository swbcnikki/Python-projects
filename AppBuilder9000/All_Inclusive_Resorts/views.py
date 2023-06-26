from django.shortcuts import render, redirect, get_object_or_404
from .models import ResortListings, ResortTraveler
from .forms import ResortListingsForm



# Create your views here.
def resorts_home(request):
    return render(request, 'All_Inclusive_Resorts/resorts_home.html')

# Story #2: Create your model ------------------------------------------------------------------------------------------

def resorts_create(request):
    form =  ResortListingsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'All_Inclusive_Resorts/resorts_create.html', content)

def resorts_read(request):
    resort = ResortListings.Resorts.all()
    content = {'resort':resort}
    return render(request, 'All_Inclusive_Resorts/resorts_read.html', content)


