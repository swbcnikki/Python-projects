from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlacesForm
from .models import Places


def seattle_home(request):
    return render(request, 'Seattle/seattle_home.html')


def seattle_create(request):
    form = PlacesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('seattle_home')
    content = {'form': form}
    return render(request, 'Seattle/seattle_create.html', content)


def seattle_view(request):
    place = Places.PlacesManager.all()
    content = {'place': place}
    return render(request, 'Seattle/seattle_view.html', content)


def seattle_details(request, pk):
    place = get_object_or_404(Places, pk=pk)
    content = {'place': place}
    return render(request, 'Seattle/seattle_details.html', content)
