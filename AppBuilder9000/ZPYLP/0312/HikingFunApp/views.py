from django.shortcuts import render, get_object_or_404
from .forms import NewTrailForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Trails

from bs4 import BeautifulSoup
import requests

# This method takes to the homepage of the app.
def home(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/HikingFunApp_home.html", context)

# This method creates a form where the user can add a trail to the templates.
def new_trail(request):
    # create object of form
    form = NewTrailForm(request.POST or None)
    # check if form data is valid
    if form.is_valid():
        #save is like inserting into templates
        form.save()

        return redirect('added_trails')
    else:
        print(form.errors)
        # form = NewTrailForm()
    trails = Trails.objects.all()

    context = {'form': form, 'trails': trails, }
    return render(request, "HikingFunApp/new_trail.html", context)

# This method helps the webpage to show all the trails in the templates.
def see_trails(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/see_trails.html", context)

# This method renders to html page that shows a  message that you successfully added a trial.
def added_trails(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/added_trails.html", context)

# This method shows the details of the trail link that is clicked from the side bar
def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Trails, pk=pk)
    form = NewTrailForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('see_trails')
        else:
            print(form.errors)
    else:
        return render(request, "HikingFunApp/get.html", {'form': form, 'item': item})

# This method gives the trails info  to webpage that displays the sidebar.
def side_bar(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/side_bar.html", context)



# If the item with this pk doesn't exist, throw error, if it exists, and method of submitting is POST
# delete and go back to trails list. Else go to confirm deletion from the user.
def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Trails, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('see_trails')
    context = {"item": item, }
    return render(request, "HikingFunApp/confirm_delete.html", context)

# This method confirms that the user wants to delete the trail item.
def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = NewTrailForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('hiking_home')
    else:
        return redirect("see_trails")

# This method uses a website and scrapes the relevant information to pass to web_scraping.html
def web_scraping(request):
    page = requests.get("https://seattle.curbed.com/maps/seattle-easy-hiking-trails-for-beginners")
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.prettify()
    trail_names = soup.find_all('h1')
    mylist= []
    for i in range(len(trail_names)):
        print(trail_names[i].get_text())
        mylist.append(trail_names[i].get_text())
    context = {'trail_names': mylist, }
    return render(request, "HikingFunApp/web_scraping.html", context)
