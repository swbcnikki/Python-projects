from django.shortcuts import render, redirect, get_object_or_404
from .forms import TravelDestinationsForm
from.models import TravelDestinations

# Create your views here.
def TravelDestinationshome(request):
    context = {}
    return render(request, 'TravelDestinations/TravelDestinations_home.html', context)

def TravelDestinationsadd(request):
    if request.method == 'POST':
        form = TravelDestinationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TravelDestinations_add')
        else:
            form = TravelDestinationsForm(request.POST)
            return render(request, 'TravelDestinations/TravelDestinations_add.html',
                          {'form': form})
    else:
        form = TravelDestinationsForm(None)
        return render(request, 'TravelDestinations/TravelDestinations_add.html', {'form': form})


def TravelDestinationsviews(request):
    views = TravelDestinations.objects.all()
    context = {'views': views}
    return render(request, 'TravelDestinations/TravelDestinations_views.html', context)

def TravelDestinationsdetail(request, pk):
    TravelDestinations_detail = get_object_or_404(TravelDestinations, pk=pk)
    views = {'TravelDestinations_detail': TravelDestinations_detail}
    context = views
    return render(request, "TravelDestinations/TravelDestinations_detail.html", context)
