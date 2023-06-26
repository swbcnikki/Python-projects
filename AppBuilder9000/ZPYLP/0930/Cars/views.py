from django.shortcuts import render,redirect,get_object_or_404
from .models import description
from .forms import descriptionForm



def Cars(request):
    return render(request, 'CarsHome.html')


def CarCreate(request):
    form = descriptionForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('Carhome')
    else:
        return render(request, 'CarCreate.html', {'form': form})

def CarsEntries(request):
    CarsEntries = description.objects.all()
    content = {'CarsEntries': CarsEntries}
    return render(request, 'CarsEntries.html', content)


def CarsView(request):
    reviews = description.objects.all()
    return render(request, 'CarsEntries.html', {'reviews': reviews})


# Allows data for one item to be viewed
def CarsDetails(request, pk):
    details = description.objects.get(pk=pk)
    return render(request, "CarsDetails.html", {'details': details})


# Delete db items
def review_delete(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('gamereviews_displayitems')
    return render(request, 'VideoGameReviews/gamereviews_delete.html', {'item': item, 'form': form})


# Edit db items
def review_edit(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gamereviews_displayitems')
    content = {'form': form}
    return render(request, 'VideoGameReviews/gamereviews_edit.html', content)