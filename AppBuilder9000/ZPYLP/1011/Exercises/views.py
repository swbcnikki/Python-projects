from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExercisesForm
# pulls in the data from our class Exercises
from .models import Exercises

# user requests page, while the server returns by rendering the webpage through the request

def exercises_home(request):
    return render(request, 'exercises_home.html', {})


def exercises_names(request):
    # this accesses our dB by calling names
    names = Exercises.objects.all()
    # inside the key, names, the value is pulling everything from Exercises
    return render(request, 'exercises_names.html', {'names': names})


def exercises_details(request, pk):
    # pk provides extra info on exercise
    # string value becomes numeric
    pk = int(pk)
    # if the item doesn't exist, 404 will be displayed
    item = get_object_or_404(Exercises, pk=pk)
    # invoke form via Post method, the instance will be item providing the exercise
    form = ExercisesForm(data=request.POST or None, instance=item)
    # if form is post and valid, the form will be saved in database
    if request.method == 'POST':
        # this is new information that will be saved from user input
        # Edit exercise form
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('exercises_names')
        else:
            print(form.errors)
    else:
        return render(request, 'exercises_details.html', {'form': form})


def exercises_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Exercises, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('exercises_names')
    context = {"item": item}
    return render(request, 'exercises_delete.html', context)

# user request to confirm deleting exercise
def exercises_confirm(request):
    if request.method == 'POST':
        form = ExercisesForm(request.POST or None)
        if form.is_valid():
            # deletes record from dB
            form.delete()
            return redirect('exercises_names')
    else:
        return redirect('exercises_names')


def exercises_create(request):
    form = ExercisesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('exercises_create')
    else:
        print(form.errors)
        form = ExercisesForm()
        context = {
            'form': form,
        }
    return render(request, 'exercises_create.html', context)
