from django.shortcuts import get_object_or_404, render,redirect
from .forms import TentForm
from .models import Tent


def Camping_Supplies_Home(request):
    #this function will take the request object and use it to find and display the Camping_Supplies_Home.html

    return render(request, 'Camping_Supplies_Home.html')

def Camping_Supplies_Create(request):
    form = TentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('Camping_Supplies_Create')
    else:
        print(form.errors)
        form = TentForm
        context = {'form': form}
    return render(request, 'create.html', context)

def SuppliesList(request):
    Tents = Tent.object.all()
    return render(request, 'SuppliesList.html', {'Tents': Tents})

def Tent_Details(request, pk):
    details = get_object_or_404(Tent, pk=pk)
    #dictionary
    context = {'details': details}
    return render(request, 'Camping_Supplies_Details.html', context)

def Tent_Delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Tent, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Camping_Supplies_Home')
    context = {"item": item}
    return render(request, "Camping_Supplies_Delete.html", context) #needs to be html


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = TentForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('Camping_Supplies_Home')
    else:
        return redirect('Camping_Supplies_Home')

def Tent_Edit(request, pk):
        site = get_object_or_404(Tent, pk=pk)
        form = TentForm(data=request.POST or None, instance=site)
        if request.method == 'POST':
            if form.is_valid():
                form2 = form.save(commit=False)
                form2.save()
                return redirect('SuppliesList')
            else:
                print(form.errors)
        else:
            return render(request, 'Camping_Supplies_Edit.html', {'form': form, 'site': site})




