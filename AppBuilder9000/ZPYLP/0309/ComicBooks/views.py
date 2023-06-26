from django.shortcuts import render, redirect
from .froms import ComicForm
from .models import Cbooks


def ComBooks(request):
    return render(request, 'ComicBooks/ComicBooks_home.html')


def forSale(request):
    form = ComicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ComicBooks_index')
    formset = {'form': form}
    return render(request, 'ComicBooks/ComicBooks_forsale.html', formset)


def ComIndex(request):
    comics = Cbooks.objects.all()
    print(comics)
    context = {'comic': comics}
    return render(request, 'ComicBooks/ComicBooks_index.html', context)


def Cominfo(request, pk):
    return render(request, 'ComicBooks/ComicsBooks_info.html', {
        'Cbooks': Cbooks.objects.get(pk=pk)
    })


def forSale(request):
    form = ComicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ComicBooks_index')
    formset = {'form': form}
    return render(request, 'ComicBooks/ComicBooks_forsale.html', formset)


def ComIndex(request):
    comics = Cbooks.objects.all()
    print(comics)
    context = {'comic': comics}
    return render(request, 'ComicBooks/ComicBooks_index.html', context)


def Cominfo(request, pk):
    return render(request, 'ComicBooks/ComicsBooks_info.html', {
        'Cbooks': Cbooks.objects.get(pk=pk)
    })


def forSale(request):
    form = ComicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ComicBooks_index')
    formset = {'form': form}
    return render(request, 'ComicBooks/ComicBooks_forsale.html', formset)


def ComIndex(request):
    comics = Cbooks.objects.all()
    print(comics)
    context = {'comic': comics}
    return render(request, 'ComicBooks/ComicBooks_index.html', context)


def Cominfo(request, pk):
    return render(request, 'ComicBooks/ComicsBooks_info.html', {
        'Cbooks': Cbooks.objects.get(pk=pk)
    })
