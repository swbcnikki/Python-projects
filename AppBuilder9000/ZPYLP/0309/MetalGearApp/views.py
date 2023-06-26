from django.shortcuts import render, get_object_or_404, redirect
from .models import DiamondDogList
from .forms import DiamondDogListForm
from django.core.paginator import Paginator
from django.db.models.functions import Lower
import requests


def home(request):
    return render(request, 'MetalGearApp/MetalGearApp_Home.html')


def create(request):
    form = DiamondDogListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MetalGearApp_Home')
    context = {'form': form}
    return render(request, 'MetalGearApp/MetalGearApp_Create.html', context)


def index(request):
    # Retrieves all objects in templates
    dDog_list = DiamondDogList.objects.order_by(Lower('fName').asc())

    paginator = Paginator(dDog_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'MetalGearApp/MetalGearApp_Index.html', {'page_obj': page_obj})


def dogDetails(request, pk):
    pk = int(pk)
    dDog = get_object_or_404(DiamondDogList, pk=pk)
    return render(request, 'MetalGearApp/MetalGearApp_Details.html', {'dDog': dDog})