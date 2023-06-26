from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShantiesForm
from .models import SeaShanties


def shantieshome(request):
    context = {}
    return render(request, 'SeaShanties/shanties_home.html', context)


def shantiesadd(request):
    if request.method == 'POST':
        form = ShantiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shanties_add')
        else:
            form = ShantiesForm(request.POST)
            return render(request, 'SeaShanties/shanties_add.html',
                          {'form': form})
    else:
        form = ShantiesForm(None)
        return render(request, 'SeaShanties/shanties_add.html', {'form': form})


def shantiesdisplay(request):
    songs = SeaShanties.objects.all()
    return render(request, 'SeaShanties/shanties_display.html', {'songs': songs})


def shantiesdetails(request, pk):
    pk = int(pk)
    song = SeaShanties.objects.filter(pk=pk)
    context = {'song': song}
    return render(request, 'SeaShanties/shanties_details.html', context)