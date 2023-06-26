from django.shortcuts import render, redirect, get_object_or_404
from .forms import ToolForm
from .models import Tool


# Displays the home page
def Blacksmithing_Home(request):
    return render(request, 'Blacksmithing/musicfiles_home.html')


# Function for user to create a Db entry
def Tool_Create(request):
    form = ToolForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect("Tool_Create")

    return render(request, 'Blacksmithing/Tool_Create.html', {"form": form})


# Function to retrieve all items from our Db
def View_Tools(request):
    # gets all objects of the Tool database unsorted
    tool_list = Tool.objects.all()

    return render(request, 'Blacksmithing/Tool_View.html', {'tool_list': tool_list})


# Function to allow user to view a single item
def Tool_Details(request, pk):
    details = get_object_or_404(Tool, pk=pk)
    return render(request, "Blacksmithing/Tool_Details.html", {'details': details})


# Function to edit an entry
def Edit_Tools(request, pk):
    item = get_object_or_404(Tool, pk=pk)
    form = ToolForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("View_Tools")
    content = {'form': form}
    return render(request, 'Blacksmithing/Tool_Edit.html', content)


# Function to delete an entry
def Delete_Tools(request, pk):
    item = get_object_or_404(Tool, pk=pk)
    form = ToolForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect("Tool_View")
    content = {'form': form}
    return render(request, 'Blacksmithing/Tool_Delete.html', {'item': item}, content)
