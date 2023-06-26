from django.shortcuts import render, get_object_or_404, redirect
from .forms import BreweryForm
from .models import Brewery, AllBreweries






# render homepage
def BA_home(request):
    return render(request, 'BreweriesApp/BreweriesApp_home.html')


# create and save new brewery
def BA_addnew(request):
    form = BreweryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('BA_addnew')
    else:
        print(form.errors)
        form = BreweryForm()
    context = {
        'form': form,
    }
    return render(request, 'BreweriesApp/BreweriesApp_addnew.html', context)


# render all breweries, change sorting between asc/desc by clicking table headers
def BA_index(request):
    orderby = request.GET.get('order_by', 'name')
    sortby = request.GET.get('sort', 'ascending')
    if sortby == 'descending':
        allbreweries = Brewery.objects.all().order_by('-' + orderby)#appends and saves new state to context
        sortby = "ascending" #change the url to descedning
    elif sortby == "ascending":
        allbreweries = Brewery.objects.all().order_by(orderby)#appends and saves new state to context
        sortby = "descending" #changes the url to descening
    context = { 'allbreweries': allbreweries, 'sortby': sortby}
    return render(request, 'BreweriesApp/BreweriesApp_index.html', context)


# render details page
def BA_details(request, _id):
    try:
        details = Brewery.objects.get(id=_id)
    except Brewery.DoesNotExist:
        raise get_object_or_404('Brewery does not exist!')

    return render(request, 'BreweriesApp/BreweriesApp_details.html', context={'details': details})


