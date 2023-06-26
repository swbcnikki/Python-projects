from django.views.generic import FormView
from .models import Files
from .forms import FileForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


# Create your views here.


def musicfiles_home(request):
    #This render function will take the request argument, and return the html document as a response

    return render(request, "musicfiles_home.html")


def musicfiles_create(request):
    form = FileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Create')
    else:
        print(form.errors)
        form = FileForm()
    context = {
        'form': form,
    }
    return render(request, 'musicfiles_create.html', context)


#returns all files within the database


def all_files_view(request):
    obj = Files.objects.all()
    return render(request, 'musicfiles_list.html', {'file_list': obj})


def musicFileDetails(request, pk):
    details = get_object_or_404(Files, pk=pk)
    context = {'details': details}
    return render(request, 'musicfiles_details.html', context)



