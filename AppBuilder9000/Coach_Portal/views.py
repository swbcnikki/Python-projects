from django.shortcuts import render, redirect, get_object_or_404
from bs4 import BeautifulSoup
from .forms import coachForm, childForm
from .models import Coach, Child
import requests

#this is the home function
def coachHome(request):
    form = coachForm(data=request.POST or None)
    if request.method == 'POST':
        return coachCreate(request)
    content = {'form': form}
    return render(request, 'Coach_Portal/coachHome.html', content)

#this is the coach create-account function with the form attached
def coachCreate(request):
    form = coachForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('coachHome')
    content = {'form': form}
    return render(request, 'Coach_Portal/coachCreate.html', content)

#this is the child create-account function with the form attached
def childCreate(request):
    form = childForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('coachHome')
    content = {'form': form}
    return render(request, 'Coach_Portal/coachChildCreate.html', content)

#this is the simple child roster sorted by grade
def childRoster(request):
    rosterList = Child.Children.all().order_by('Child_Grade')
    content = {'rosterList': rosterList}
    return render(request, 'Coach_Portal/coachChildRoster.html', content)

#this is the child details function where more information can be seen of each child in the database
def childDetails(request, pk):
    details = get_object_or_404(Child, pk=pk)
    content = {'details': details}
    return render(request, 'Coach_Portal/coachChildDetails.html', content)

#this is the child-update function, where each line of information is turned into a form and can be reposted back into the database
def childUpdate(request, pk):
    details = Child.Children.get(pk=pk)
    form = childForm(request.POST or None, instance=details)

    if form.is_valid():
        form.save()
        return redirect('coachChildRoster')

    content = {'details': details, 'form': form}
    return render(request, 'Coach_Portal/coachUpdateChild.html',content)

#this is the child delete-account function
def childDelete(request, pk):
    childForDelete = get_object_or_404(Child, pk=pk)

    if request.method == "POST":
        childForDelete.delete()
        return redirect('coachChildRoster')
    content = {'childForDelete': childForDelete}
    return render(request, 'Coach_Portal/coachChildDelete.html', content)

#These variables and the subsequent 'addChildren' function add some kids to the roster IF the roster is empty. Helpful to view demo functionality!
cFName = ['Aman', 'Vijay', 'Casey', 'Katelyn', 'Jessica', 'Chris', 'Lacy', 'Luis']
cLName = ['Jones', 'Vitali', 'Adams', 'Flaherty', 'Jones', 'Cringle', 'Lewis', 'Lopez']
cGrade = ['K-1st', 'K-1st', '2nd-3rd', '2nd-3rd', '4th-5th', '4th-5th', '6th-7th', '6th-7th']
cJersey = [10,23,45,34,56,67,10,15]
pName = ['Bob Jones', 'Pchenka Vitali', 'Phil Adams', 'Laura Flaherty', 'Jason Jones', 'Mrs. Cringle', 'Samantha Lewis']
pPhone = [5033458567,5033678567,5033456798,5032345467,5031459689,5452456567,5034576833,5031234567]
pEmail = ['Bob@gmail.com', 'Pchenka@gmail.com', 'Phil@gmail.com', 'Laura@gmail.com', 'Jason@gmail.com', 'naughtyornice@gmail.com', 'Lulu@gmail.com']
notesOrAllergies = ['Bob@gmail.com', 'Pchenka@gmail.com', 'Phil@gmail.com', 'Laura@gmail.com', 'Jason@gmail.com', 'naughtyornice@gmail.com', 'Lulu@gmail.com']


def addChildren(request, *args, **kwargs):
    for i in range(len(cFName)):
        Child.children.create(First_Name=cFName[i], Last_Name=cLName[i], Child_Grade=cGrade[i])


# Beautiful soup used to pull field availability
def fieldSoup(request):
    dates = []  # Dates =

    page = requests.get("https://apm.activecommunities.com/clarkcountyparks/Facility_Search?IsCalendar=true&facility_id=61&year=2022&month=5&startyear=2022&endyear=2027")
    soup = BeautifulSoup(page.content, 'html.parser')
    free = soup.find_all('td class')
    booked = soup.find_all('strong')

    for i in dates:
        dateList = i.text.strip()
        dates.append(dateList)
    #l = chars[6], chars[7]  # Grabs the elements that need to be joined.
    #fix = ' '.join(l)  # Joins the two elements and places them in a variable
    #chars.insert(6, fix)  # Inserts joined elements into array at appropriate index
    #del chars[8]  # Removes unnecessary element
    #del chars[7]  # Removes unnecessary element

    content = {'dates': dates}
    return render(request, '', content)

