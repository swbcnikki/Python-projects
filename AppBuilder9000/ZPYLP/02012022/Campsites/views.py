from django.shortcuts import get_object_or_404, redirect, render

from .form import CampsitesForm
from .models import CampSites


def campsites_home(request):
    return render(request, 'campsites_home.html')


def add_campsites(request):
    form = CampsitesForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('campsites_list')
    else:
        print(form.errors)
        form = CampsitesForm
        context = {'form': form}
    return render(request, 'campsites_create.html', context)


def list_campsites(request):
    campsites = CampSites.objects.all()
    return render(request, 'campsites_list.html', {'campsites': campsites})


def campsites_details(request, pk):
    details = get_object_or_404(CampSites, pk=pk)
    context = {'details': details}
    return render(request, 'campsites_details.html', context)


def edit_site(request, pk):
    site = get_object_or_404(CampSites, pk=pk)
    form = CampsitesForm(data=request.POST or None, instance=site)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('campsites_list')
        else:
            print(form.errors)
    else:
        return render(request, 'edit_site.html', {'form': form, 'site': site})


# update view for details
def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(CampSites, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('campsites_list')
    context = {"item": item}
    return render(request, "campsites_delete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = CampsitesForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('campsites_list')
    else:
        return redirect('campsites_list')
