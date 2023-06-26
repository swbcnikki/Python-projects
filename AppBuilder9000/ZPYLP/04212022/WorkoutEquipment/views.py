from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkoutEquipment
from .forms import WorkoutEquipmentForm
from bs4 import BeautifulSoup
import json
import requests




# function to render Homepage
def workout_equipment_home(request):
    products = WorkoutEquipment.objects.all()
    return render(request, "WorkoutEquipment/WorkoutEquipHome.html", {'products': products})


def workout_equip_console(request):
    # if POST request type then process the forms data
    form = WorkoutEquipmentForm(request.POST or None)
    # checking if the form is valid
    if form.is_valid():
        form.save()
        return redirect('WorkoutEquipHome')
    else:
        print(form.errors)   # create empty form if not filled out correctly
        form = WorkoutEquipmentForm()
    context = {
        'form': form    # context form object
    }   # pass in request object, pass in file, and pass in context variables to be returned
    return render(request, 'WorkoutEquipment/WorkoutEquipConsole.html', context)


# function to create new item in Db through form
def workout_equip_create(request):
    form = WorkoutEquipmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('workout_equip_console')
    else:
        print(form.errors)
        form = WorkoutEquipmentForm()
    context = {
        'form': form,
    }
    return render(request, 'WorkoutEquipment/WorkoutEquipCreate.html', context)


# function to display items in WorkoutEquipDisplay.html
# ("Your collection" button navbar) content dictionary = all WorkoutEquipment objects
def workout_equip_display(request):
    display_items = WorkoutEquipment.objects.all()
    content = {'display_items': display_items}
    return render(request, 'WorkoutEquipment/WorkoutEquipDisplay.html', content)


# function to get object details through primary key parameter of single object
def workout_equip_details(request, pk):
    details = get_object_or_404(WorkoutEquipment, pk=pk)
    content = {'details': details}
    return render(request, 'WorkoutEquipment/WorkoutEquipDetails.html', content)


# function to get object by primary key and create form instance to edit a record in Db
def workout_equip_edit(request, pk):
    edit = get_object_or_404(WorkoutEquipment, pk=pk)  # edit is object record through primary key
    form = WorkoutEquipmentForm(data=request.POST or None, instance=edit)
    if request.method == 'POST':
        if form.is_valid():
            form.save()        # if form is valid save form instance
            return redirect('workout_equip_console')
        else:
            print(form.errors)
            form = WorkoutEquipmentForm()
    context = {
        'form': form, 'edit': edit
    }
    return render(request, 'WorkoutEquipment/WorkoutEquipEdit.html', context)


# function to delete object through pk and form instance, deletes item object/form instance
def workout_equip_delete(request, pk):
    item = get_object_or_404(WorkoutEquipment, pk=pk)
    form = WorkoutEquipmentForm (data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('workout_equip_display')
    return render(request, 'WorkoutEquipment/WorkoutEquipDelete.html', {'item': item, 'form': form})


# function confirming deletion of record returning user to console page afterward
def confirmed(request):
    if request.method == 'POST':
        # created form instance and binds data to it
        form = WorkoutEquipmentForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('workout_equip_console')
    else:
        return redirect('workout_equip_console')

# This function uses beautiful soup methods to isolate data on a webpage and takes that content
# for display on bsdisplay template page


def workout_equip_bs_display(request):   # scraping website used fitness sales with blog info using beautiful soup
    bsinfo = requests.get("https://www.usedfitnesssales.com/chooschoosing-your-best-new-home-gym-fitness-equipment-for-the-new-yearing-your-best-new-home-gym-fitness-equipment-for-the-new-year/")
    c = BeautifulSoup(bsinfo.content, 'html.parser')
    title = c.find(class_='entry-title fusion-post-title').get_text()
    blogP = c.find(class_='post-content').get_text()
    content = {'bsinfo': bsinfo, 'title': title, 'blogP': blogP}
    return render(request, 'WorkoutEquipment/WorkoutEquipBsDisplay.html', content)

# function to display api results on template page
# *** going to fix with assistance in the future to parse isolated sections of data
def workout_equip_display_api(request):

    url = "https://exercisedb.p.rapidapi.com/exercises"

    headers = {
        'x-rapidapi-host': "exercisedb.p.rapidapi.com",
        'x-rapidapi-key': "748396d4admsh94a5c03979cf998p1b51c9jsn2ffa0b95942a"
    }
    response = requests.request("GET", url, headers=headers)
    workout_info = json.loads(response.text)
    pr = json.dumps(workout_info, indent=4)
    print(pr)
    context = {
        'pr': pr
    }
    return render(request, 'WorkoutEquipment/WorkoutEquipDisplayAPI.html', context)








