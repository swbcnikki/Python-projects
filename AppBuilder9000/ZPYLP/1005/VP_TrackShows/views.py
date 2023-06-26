from django.shortcuts import render, get_object_or_404, redirect
from .models import MyShows
from .forms import ShowForm


def home(request):
    return render(request, 'VP_TrackShows/musicfiles_home.html')


def allshows(request):
    allshows = MyShows.objects.all()
    context = {'allshows': allshows}
    return render(request, 'VP_TrackShows/allshows.html', context)


def details(request, pk):
    details = get_object_or_404(MyShows, pk=pk)
    context = {'details': details}
    return render(request, "VP_TrackShows/details.html", context)


def delete(request, pk):  # tests for delete work well.
    item = get_object_or_404(MyShows, pk=pk)
    form = ShowForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect("allshows")
    context = {'item': item, 'form': form}
    return render(request, 'VP_TrackShows/delete.html', context)


def edit(request, pk):  # tests for edits work well.
    item = get_object_or_404(MyShows, pk=pk)
    form = ShowForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("allshows")
    context = {'form': form}
    return render(request, 'VP_TrackShows/edit.html', context)


def create(request):
    form = ShowForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('allshows')
    else:
        context = {'form': form}
        return render(request, 'VP_TrackShows/create.html', context)
