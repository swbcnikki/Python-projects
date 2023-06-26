from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from django.views.generic import FormView
from .models import Yoga
from .forms import YogaForm


# Adding function to render home page.
def home(request):
    return render(request, 'Practicing_Yoga/yoga_home.html')

def create(request):
    form = YogaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('yoga_create')
    else:
        print(form.errors)
        form = YogaForm()
    context = {
        'form': form,
    }
    return render(request, 'Practicing_Yoga/yoga_create.html', context)

def items(request):
    obj = Yoga.objects.all()
    return render(request, 'Practicing_Yoga/yoga_items.html', {'obj': obj})

def details(request, pk):
    details = get_object_or_404(Yoga, pk=pk)
    context = {'details': details}
    return render(request, 'Practicing_Yoga/yoga_details.html', context)
