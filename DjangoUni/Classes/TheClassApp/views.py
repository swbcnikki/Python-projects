from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ClassesForm
from .models import djangoClasses
from django.shortcuts import render, redirect, get_object_or_404
from .models import djangoClasses
from .forms import ClassesForm, CreateForm



# Create views here.

def admin_console(request):
    TheClassApp = djangoClasses.objects.all()
    return render(request, 'TheClassApp/createRecord.html', {'TheClassApp': TheClassApp})


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


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(djangoClasses, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {'item': item}
    return render(request, 'admin_console', context)

def createRecord(request):
    form = CreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = CreateForm()
    context = {'form': form}
    return render(request, 'TheClassApp/createRecord.html', context)