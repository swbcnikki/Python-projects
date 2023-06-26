from django.shortcuts import render, get_object_or_404, redirect

from .forms import HardRockForm
from .models import HardRock


# Create your views here.


def RocksHome(request):
    return render(request, 'Rock/RocksHome.html')


def HardRock_List(request):
    list = HardRock.objects.all()
    return render(request, 'Rock/HardRock_List.html', {'list': list})


def Rock_Create(request):
    form = HardRockForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('RocksHome')
    content = {'form': form}
    return render(request, 'Rock/Rock_Create.html', content)


def HardRock_Details(request):
    return render(request, 'Rock/HardRock_Details.html')


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(HardRock, pk=pk)
    form = HardRockForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('HardRock_List')
        else:
            print(form.errors)
    else:
        return render(request, 'Rock/HardRock_Details.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(HardRock, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('HardRock_List')
    context = {"item": item}
    return render(request, "Rock/confirm_Delete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = HardRockForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('HardRock_List')
    else:
        return redirect('HardRock_List')
