from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import RockLoc
from .forms import RockForm
from django.views.generic import FormView


def Oregon_Rocks_Home(request):
    return render(request, 'OregonRocks/OregonRocksHome.html')

def Rocks_Create(request):
    form = RockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Rocks_Create')
    else:
        print(form.errors)
        form = RockForm()
    context = {
        'form': form,
    }
    return render(request, 'OregonRocks/Rocks_Create.html', context)



def Rock_Locations(request):
    locations = RockLoc.objects.all()
    return render(request, 'OregonRocks/Rock_Locations.html', {'locations': locations})

def Rock_Details(request, pk):
    details = get_object_or_404(RockLoc, pk=pk)
    context = {'details': details}
    return render(request, "OregonRocks/Rock_Details.html", context)

def Edit(request, pk):
    item = get_object_or_404(RockLoc, pk=pk)
    form = RockForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('Rock_Locations')
        else:
            print(form.errors)
    else:
        return render(request, "OregonRocks/Edit.html", {'form': form, 'item':item})

def update(request, pk):
    rock = RockLoc.objects.get(pk=pk)
    rock.name = request.POST.get('name')
    rock.save()
    return redirect('Rock_Locations')

def confirmDel(request, pk):
    item = get_object_or_404(RockLoc, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Rock_Locations')
    context = {'item': item}
    return render(request, 'OregonRocks/confirmDel.html', context)









#geolocator = Nominatim(user_agent="location")


# class ListCreateGenericViews(generics.ListCreateAPIView):
#     queryset = get_object_or_404(RockLoc)
#     serializer_class = RockLoc
#
#     def perform_create(self, serializer):
#         address = serializer.initial_data["address"]
#         g = geolocator.geocode(address)
#         lat = g.latitude
#         lng = g.longitude
#         pnt = Point(lng, lat)
#         print(pnt)
#         serializer.save(location=pnt)
#
#
# class RockUpdateRetrieveView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_object_or_404(RockLoc)
#     serializer_class = RockLoc
#
#     def perform_update(self, serializer):
#         address = serializer.initial_data["address"]
#         g = geolocator.geocode(address)
#         lat = g.latitude
#         lng = g.longitude
#         pnt = Point(lng, lat)
#         print(pnt)
#         serializer.save(location=pnt)