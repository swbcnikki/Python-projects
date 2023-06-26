from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SharksForm
from .models import Sharks


def SharksApp_home(request):
    return render(request, "SharksApp_home.html")


def Create_Shark(request):
    form = SharksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('SharksApp_newitem')
    else:
        print(form.errors)
        form = SharksForm()
    context = {
        'form': form,
    }
    return render(request, 'SharksApp/SharksApp_newitem.html', context)


def Display_DB(request):
    all_sharks = Sharks.objects.all()
    content = {
        'all_sharks': all_sharks
    }
    return render(request, 'SharksApp/SharksApp_displaydb.html', content)


def Shark_Details(request, pk):
    pk = int(pk)
    shark = get_object_or_404(Sharks, pk=pk)
    content = {
        'shark': shark
    }
    return render(request, 'SharksApp/SharksApp_detailspage.html', content)


def Edit_Shark(request, pk):
    pk = int(pk)
    shark = get_object_or_404(Sharks, pk=pk)
    if request.method == "POST":
        form = SharksForm(data=request.POST, instance=shark)
        if form.is_valid():
            form_update = form.save(commit=False)
            form_update.save()
            return redirect('SharksApp_detailspage', pk=shark.pk)
    else:
        form = SharksForm(instance=shark)
    content = {
         'form': form
    }
    return render(request, 'SharksApp/SharksApp_editpage.html', content)


def Delete_Shark(request, pk):
    pk = int(pk)
    shark = get_object_or_404(Sharks, pk=pk)
    if request.method == "POST":
        shark.delete()
        return redirect('SharksApp_displaydb')
    return render(request, 'SharksApp/SharksApp_deletepage.html')

