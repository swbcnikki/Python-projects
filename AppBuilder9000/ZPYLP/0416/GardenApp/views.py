from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlannerForm, TrackerForm
from .models import Planner, Tracker



# Create your views here.
def gardenhome(request):
    context = {}
    return render(request, 'GardenApp/garden_home.html', context)

def createplanner(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardenplanner')
        else:
            form = PlannerForm(request.POST)
            return render(request, 'GardenApp/garden_planner.html',
                          {'form': form})  # pass form to render on gardenplanner.html
    else:
        form = PlannerForm(None)
        return render(request, 'GardenApp/garden_planner.html', {'form': form})

def createtracker(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardentracker')
        else:
            form = TrackerForm()
            return render(request, 'GardenApp/garden_tracker.html', {'form': form})
    else:
        form = TrackerForm(None)
        return render(request, 'GardenApp/garden_tracker.html', {'form': form})

def allvegetables(request):
    plan = Planner.objects.all()
    track = Tracker.objects.all()
    context = {'plan': plan, 'track': track}
    return render(request, 'GardenApp/garden_allvegetables.html', context)

def plannerdetails(request, pk):
    pk = int(pk)
    plan = get_object_or_404(Planner, pk=pk)
    track = Tracker.objects.all()
    context = {'plan': plan, 'track': track}
    return render(request, 'GardenApp/planner_details.html', context)

def trackerdetails(request, pk):
    pk = int(pk)
    track = get_object_or_404(Tracker, pk=pk)
    plan = Planner.objects.all()
    context = {'track': track, 'plan': plan}
    return render(request, 'GardenApp/tracker_details.html', context)

def planneredit(request, pk):
    pk = int(pk)
    plan = get_object_or_404(Planner, pk=pk)
    form = PlannerForm(request.POST, instance=plan)
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('plannerdetails', pk)
    else:
        form = PlannerForm(None, instance=plan)
    return render(request, 'GardenApp/planner_edit.html', {'plan':plan, 'form': form})

def trackeredit(request, pk):
    pk = int(pk)
    track = get_object_or_404(Tracker, pk=pk)
    form = TrackerForm(request.POST, instance=track)
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('trackerdetails', pk)
    else:
        form = TrackerForm(None, instance=track)
    return render(request, 'GardenApp/tracker_edit.html', {'track':track, 'form': form})

def plannerdelete(request, pk):
    pk = int(pk)
    plan = get_object_or_404(Planner, pk=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('allvegetables')
    context = {'plan': plan}
    return render(request, 'GardenApp/planner_delete.html', context)

def trackerdelete(request, pk):
    pk = int(pk)
    track = get_object_or_404(Tracker, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('allvegetables')
    context = {'track': track}
    return render(request, 'GardenApp/tracker_delete.html', context)