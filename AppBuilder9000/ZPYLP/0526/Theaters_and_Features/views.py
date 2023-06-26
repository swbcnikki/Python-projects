from django.shortcuts import render, redirect, get_object_or_404
from .forms import TheaterForm
from .models import Theaters
# Create your views here.



def Theater_home(request):
    return render(request, 'Theaters_and_Features/Theaters_and_Features_home.html')


def new_Theater(request):
    form = TheaterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('new_Theater')
    context = {'form': form}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_add.html', context)


def find_Theater(request):
    all_theaters = Theaters.objects.all
    context = {'all_theaters': all_theaters}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_find.html', context)


def Theater_details(request, pk):
    pk = int(pk)
    get_theaters = Theaters.objects.filter(pk=pk)
    context = {'get_theaters': get_theaters}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_detail.html', context)

def edit_details(request, pk):
    pk = int(pk)
    edit_theaters = get_object_or_404(Theaters, pk=pk)
    if request.method == "POST":
        form = TheaterForm(data=request.POST, instance=edit_theaters)
        if form.is_valid():
            form_update = form.save(commit=False)
            form_update.save()
            return redirect('Theater_details', pk=edit_theaters.pk)
    else:
        form = TheaterForm(instance=edit_theaters)
    context = {'form': form}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_edit.html', context)

def delete_Theater(request, pk):
    pk = int(pk)
    edit_theaters = get_object_or_404(Theaters, pk=pk)
    context = {"edit_theaters": edit_theaters}
    if request.method == 'POST':
        edit_theaters.delete()
        return redirect("find_Theater")
    return render(request, 'Theaters_and_Features/Theaters_and_Features_delete.html', context)







