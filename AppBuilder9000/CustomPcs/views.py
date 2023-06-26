from django.shortcuts import render, redirect, get_object_or_404
from .models import Builds
from .forms import BuildForm


# Creating the views

def CustomPcs_home(request):
    return render(request, 'CustomPCs/CustomPcs_home.html')


def CreateEntry(request):
    form = BuildForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    else:
        print(form.errors)
        content = {'form': form}
        return render(request, 'CustomPcs/BuildForm.html', content)
