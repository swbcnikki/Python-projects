from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import TheForce
from .forms import TheForceForm
from django.views.generic import FormView

# Create your views here.
def The_Force_home(request):
    return render(request, 'The_Force_Home.html')

def The_Force_Create(request):
        form = TheForceForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('TheForce')

        else:
            print(form.errors)
            form = TheForceForm()
        context = {
            'form': form,
        }
        return render(request, 'The_Force_Create.html', context)



def The_Force_Events(request):
    Event = TheForce.objects.all()
    return render(request, 'The_Force_Event.html', {'Event': Event})



def Edit(request, pk):
    item = get_object_or_404(TheForce, pk=pk)
    form = TheForceForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('Event')

        else:
            print(form.errors)
    else:
        return render(request, 'The_Force_Create.html', {'form': form, 'item': item})


def The_Force_Details(request, pk):
    Details = get_object_or_404(TheForce, pk=pk)
    context = {'Details': Details}
    return render(request, "The_Force_Details.html", context)




def ConfirmDelete(request, pk):
    item = get_object_or_404(TheForce, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Event')
    context = {'item': item}
    return render(request, 'The_Force_ConfirmDelete.html', context)







