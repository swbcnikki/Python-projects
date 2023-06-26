from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


# Create your views here.
def Character_home(request):
    return render(request, "Character_home.html")


def Character_add(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # google.com is a placeholder for the viewing file for the objects
            return redirect(Character_list)
        else:
            content = {'form': form}
            return render(request, 'Character_add.html', content)
    content = {'form': form}
    return render(request, 'Character_add.html', content)


def Character_list(request):
    Character_all = Character_create.objects.all()
    context = {'Character_all': Character_all}
    return render(request, 'Character_view.html', context)


def Character_details(request, pk):
    Character_get = get_object_or_404(Character_create, pk=pk)
    Character_all = {'Character_get': Character_get}
    context = Character_all
    return render(request, 'Character_details.html', context)

def Character_link(request):
    Character_show = Character_create.objects.all()
    context = {'Character_show': Character_show}
    return render(request, 'Character_link.html', context)