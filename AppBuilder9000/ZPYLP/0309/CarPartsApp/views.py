from django.shortcuts import render, redirect, get_object_or_404
from .models import MyCarParts
from .forms import MyCarPartsForm

def CarPartsApp_home(request):
    return render(request, "CarPartsApp/CarPartsApp_home.html")

def CarPartsApp_AddPart(request):
    form = MyCarPartsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CarPartsApp_home')
    formset = {'form': form}
    return render(request, 'CarPartsApp/CarPartsApp_AddPart.html', formset)

def CarPartsApp_myParts(request):
    parts = MyCarParts.objects.all()
    return render(request, 'CarPartsApp/CarPartsApp_myParts.html', {'parts': parts})


def CarPartsApp_details(request, pk):
    myParts = MyCarParts.objects.get(pk=pk)
    content = {'myParts': myParts}
    return render(request, 'CarPartsApp/CarPartsApp_details.html', content)


def CarPartsApp_index(request):
    parts = MyCarParts.objects.all()
    return render(request, 'CarPartsApp/CarPartsApp_index.html', {'parts': parts})


def CarPartsApp_edit(request, pk):
    pk = int(pk)
    parts = get_object_or_404(MyCarParts, pk=pk)
    form = MyCarPartsForm(data=request.POST or None, instance=parts)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('CarPartsApp_myParts')
        else:
            print(form.errors)
    else:
        context = {'parts': parts, 'form': form}
        return render(request, 'CarPartsApp/CarPartsApp_edit.html', context)

def CarPartsApp_delete(request, pk):
    pk = int(pk)
    parts = get_object_or_404(MyCarParts, pk=pk)
    if request.method == 'POST':
        parts.delete()
        return redirect('CarPartsApp_myParts')
    else:
        return render(request, 'CarPartsApp/CarPartsApp_confirmedDelete.html') #pk

def CarPartsApp_confirmedDelete(request):
    if request.method == 'POST':
        form = MyCarPartsForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('CarPartsApp_myParts')
        else:
            return render(request, 'CarPartsApp/CarPartsApp_confirmedDelete.html')

