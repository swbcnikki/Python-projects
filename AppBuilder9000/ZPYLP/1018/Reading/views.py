from django.shortcuts import render, redirect, get_object_or_404
from .models import Archive
from .forms import RecordForm

# Displays the Home page
def Reading_Home(request):
    return render(request, 'Reading/Reading_Home.html')

# Creates a new Record
def Reading_Create(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Reading_Records')
    else:
        print(form.errors)
        form = RecordForm()
    context = {
        'form': form,
    }
    return render(request, 'Reading/Reading_Create.html', context)

# View all Resources added to Database
def Reading_Records(request):
    records = Archive.objects.all()
    return render(request, 'Reading/Reading_Records.html', {'records': records})

# Retrieve record details
def Reading_Details(request, pk):
    details = get_object_or_404(Archive, pk=pk)
    context = {'details': details}
    return render(request, "Reading/Reading_Details.html", context)