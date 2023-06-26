from django.shortcuts import render, redirect, get_object_or_404
from .forms import TVshowsForm
from .models import TVshows
from django.core.paginator import Paginator

# this renders the home page
def TVshow_home(request):
    return render(request, "TVshowAPP/musicfiles_home.html")

# adds data to the data base
def addShow(request):
    form = TVshowsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('TVshow_home')
    else:
        print(form.errors)
        form = TVshowsForm()
    context = {
        'form': form,
    }
    return render(request, 'TVshowAPP/AddTVShow.html', context)

def seeShow(request):
    # gets all items from DB and returns info to table on TVshow_list
    tvshowdb = TVshows.objects.all()
    context = {'tvshowdb': tvshowdb}
    return render(request, 'TVshowAPP/TVShow_List.html', context)

def sortShow(request):
    # gets all items from DB, sorts by show name, and returns info to table on TVsort
    tvshowdb = TVshows.objects.all()
    sorted_shows = sorted(tvshowdb, key=lambda TVshows:TVshows.show_name)
    context = {'tvshowdb': tvshowdb, 'sorted_shows': sorted_shows}
    return render(request, 'TVshowAPP/TVsort.html', context)

def sortGenre(request):
    # gets all items from DB, sorts by genre, and returns info to table on TVsortg
    tvshowdb = TVshows.objects.all()
    sorted_shows = sorted(tvshowdb, key=lambda TVshows:TVshows.genre)
    context = {'tvshowdb': tvshowdb, 'sorted_shows': sorted_shows}
    return render(request, 'TVshowAPP/TVsortg.html', context)


def showIndex(request):
    # sends you to the index page and displays what is in the db, also activates paginator
    tvshow = TVshowsForm()
    tvshowdb = TVshows.objects.all()
    page = Paginator(tvshowdb, 10)
    page_show = request.GET.get('page')
    page2 = page.get_page(page_show)
    context = {'tvshow': tvshow, 'tvshowdb': tvshowdb}
    return render(request, 'TVshowAPP/TVshow_index.html', {'page2': page2}, context)

def showDetails(request, pk):
    # this function locates the pk, sends the info the details page
    pk = int(pk)
    tvshow = get_object_or_404(TVshows, pk=pk)
    tvform = TVshowsForm(data=request.POST or None, instance=tvshow)
    return render(request, 'TVshowAPP/TVshow_details.html', {'tvform': tvform})




  #  if request.method == 'POST':
   #     if tvform.is_valid():
    #        tvform2 = form.save(commit=False)
     #       tvform2.save()
      #      return redirect('showIndex')
       # else:
        #    print(tvform.errors)
    #else:
