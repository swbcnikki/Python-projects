from django.shortcuts import render, get_object_or_404, redirect
from .forms import CultClassicsForm
from .models import CultClassics


# Creating views
def cultclassicsHome(request):
    return render(request, 'CultClassicsHome.html')

def CultClassicsCreate(request):
    form = CultClassicsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('CultClassicsCreate')
    else:
        print(form.errors)
        form = CultClassicsForm()
    context = {'form': form}
    return render(request, 'CultClassicsCreate.html', context)

def CultClassicsMovies(request):
    cultclassics = CultClassics.objects.all()
    return render(request, 'CultClassicsMovies.html', {'cultclassics': cultclassics})

def CultClassicsDetails(request, pk):
    pk = int(pk)
    item = get_object_or_404(CultClassics, pk=pk)
    form = CultClassicsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('CultClassicsMovies')
        else:
            print(form.errors)
    else:
        return render(request, 'CultClassicsDetails.html', {'form': form})