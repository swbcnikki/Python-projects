from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource
from .forms import ResourceForm


# Displays the Home page
def EdTech_Home(request):
    resources = Resource.objects.all()
    return render(request, 'EdTech/EdTech_Home.html')

# Create new Resource
def EdTech_Create(request):
    form = ResourceForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('EdTech_Entries')
    else:
        return render(request, 'EdTech/EdTech_Create.html', {'form': form})


# View all Resources added to Database
def EdTech_Entries(request):
    entries = Resource.objects.all()
    return render(request, 'EdTech/EdTech_Entries.html', {'entries': entries})


# Retrieve resource details
def EdTech_Details(request, pk):
    details = get_object_or_404(Resource, pk=pk)
    context = {'details': details}
    return render(request, "EdTech/EdTech_Details.html", context)


# Delete a Resource
def EdTech_Delete(request, pk):
    item = get_object_or_404(Resource, pk=pk)
    form = ResourceForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect("EdTech_Entries")
    return render(request, 'EdTech/EdTech_Delete.html', {'item': item, 'form': form})


# Edit a Resource
def EdTech_Edit(request, pk):
    item = get_object_or_404(Resource, pk=pk)
    form = ResourceForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("EdTech_Entries")
    content = {'form': form}
    return render(request, 'EdTech/EdTech_Edit.html', content)
