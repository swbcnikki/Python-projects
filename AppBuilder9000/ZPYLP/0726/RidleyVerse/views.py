from bs4 import BeautifulSoup
from .forms import MovieForm
from .models import Movie
import requests
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect


# Nav Button functions.


def RidleyVersehome(request):
    return render(request, 'RidleyVerse/RidleyVerse_home.html')


def ListMovies(request):
    Movies = Movie.objects.all().order_by("FilmName")
    return render(request, "RidleyVerse/RidleyVerse_movielist.html", {'Movies': Movies})


def MovieDetails(request, id):
    Movies = get_object_or_404(Movie, id=id)
    return render(request, "RidleyVerse/RidleyVerse_details.html", {
        'name': Movies.FilmName,
        'year': Movies.ReleaseYear,
        'Starring': Movies.StarNames,
        'Directors': Movies.DirectorName,
        'Summary': Movies.MovieSummary,
    })
# End Nav Button functions.
# --------------------------------------------
# Modification controls


def AddMovies(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Add-Movies')
    else:
        form = MovieForm()
    return render(request, 'RidleyVerse/RidleyVerse_add.html', {'form': form})


def DeleteMovies(request, id):
    Movies = get_object_or_404(Movie, id=id)
    form = MovieForm(request.POST or None, instance=Movies)
    if request.method == "POST":
        Movies.delete()
        return HttpResponseRedirect('/RidleyVerse/List-Movies/')
    return render(request, "RidleyVerse/RidleyVerse_Delete.html", {"form": form})


def EditMovies(request, id):
    Movies = get_object_or_404(Movie, id=id)  # This sets the movie id base on what was chosen by the user.
    form = MovieForm(request.POST or None, instance=Movies)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/RidleyVerse/' + id)
    return render(request, "RidleyVerse/RidleyVerse_Update.html", {"form": form})
# End Modification controls


# RidleySoup Function-------------------------------------------------------------------------------------------------

def GetRidleySoup(request):
    page = requests.get("https://www.imdb.com/list/ls050064593/")
    soup = BeautifulSoup(page.content, 'html.parser')
    Allp = soup.findAll('p')

    FullPot = (
            Allp[2].text + Allp[5].text + Allp[7].text +
            Allp[10].text + Allp[17].text + Allp[20].text + Allp[22].text + Allp[25].text + Allp[27].text +
            Allp[30].text + Allp[32].text + Allp[35].text + Allp[37].text + Allp[40].text + Allp[42].text +
            Allp[45].text + Allp[47].text + Allp[50].text + Allp[52].text + Allp[55].text + Allp[57].text +
            Allp[60].text + Allp[62].text + Allp[65].text + Allp[67].text + Allp[70].text + Allp[72].text +
            Allp[75].text + Allp[77].text + Allp[80].text + Allp[82].text + Allp[85].text + Allp[87].text +
            Allp[90].text + Allp[92].text + Allp[95].text + Allp[97].text +
            Allp[100].text + Allp[102].text + Allp[105].text)

    FullPotDictionary = {'FullPot': FullPot}
    return render(request, "RidleyVerse/RidleyVerse_FullStory.html", FullPotDictionary)



"""



if __name__ == "__main__":
    GetRidleySoup()



def GetRidleySoup():
    page = requests.get("https://www.imdb.com/list/ls050064593/")
    soup = BeautifulSoup(page.content, 'html.parser')
    Allp = soup.findAll('p')
    B = "<hr>"
    print(Allp[0].text)
    print(B)
    print(Allp[2].text, Allp[5].text)
    print(B)
    print(Allp[7].text, Allp[10].text)
    print(B)
    print(Allp[12].text, Allp[15].text)
    print(B)
    print(Allp[17].text, Allp[20].text)
    print(B)
    print(Allp[22].text, Allp[25].text)
    print(B)
    print(Allp[27].text, Allp[30].text)
    print(B)
    print(Allp[32].text, Allp[35].text)
    print(B)
    print(Allp[37].text, Allp[40].text)
    print(B)
    print(Allp[42].text, Allp[45].text)
    print(B)
    print(Allp[47].text, Allp[50].text)
    print(B)
    print(Allp[52].text, Allp[55].text)
    print(B)
    print(Allp[57].text, Allp[60].text)
    print(B)
    print(Allp[62].text, Allp[65].text)
    print(B)
    print(Allp[67].text, Allp[70].text)
    print(B)
    print(Allp[72].text, Allp[75].text)
    print(B)
    print(Allp[77].text, Allp[80].text)
    print(B)
    print(Allp[82].text, Allp[85].text)
    print(B)
    print(Allp[87].text, Allp[90].text)
    print(B)
    print(Allp[92].text, Allp[95].text)
    print(B)
    print(Allp[97].text, Allp[100].text)
    print(B)
    print(Allp[102].text, Allp[105].text)
    print(B)
"""

# End Ridley Soup Function. -----------------------------------------------------------------------------------------

