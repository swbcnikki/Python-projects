from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ClassesForm
from .models import djangoClasses


# Create views here.

def admin_console(request):
    TheClassApp = djangoClasses.objects.all()
    return render(request, 'home.html', {'TheClassApp': TheClassApp})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(djangoClasses, pk=pk) #page error handling
    form = ClassesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
