from .forms import YoutuberForm
from .models import Youtuber
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
import webbrowser
from bs4 import BeautifulSoup
import requests


#  YTsubLink =

# Nav Button functions.
# ---------------------------------------------------------------------------------------------------------------------


def YTfeedhome(request):
    return render(request, 'YTfeed/YTfeed_home.html')


def ListYoutubers(request):
    Youtubers = Youtuber.objects.all().order_by("YTname")
    return render(request, "YTfeed/YTfeed_YTlist.html", {'Youtubers': Youtubers})


# End Nav Button functions.
# ---------------------------------------------------------------------------------------------------------------------
def MovieDetails(request, id):
    Movies = get_object_or_404(Movie, id=id)
    return render(request, "RidleyVerse/RidleyVerse_details.html", {
        'name': Movies.FilmName,
        'year': Movies.ReleaseYear,
        'Starring': Movies.StarNames,
        'Directors': Movies.DirectorName,
        'Summary': Movies.MovieSummary,
    })

# BS Testing


def GetYTSoup():
    page = requests.get("https://www.apmex.com")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_s = soup.findAll('div')

    SilverSpot = div_s[6].find('span', class_="current").text
    GoldSpot = div_s[4].find('span', class_="current").text
    PlatinumSpot = div_s[8].find('span', class_="current").text

    print(SilverSpot)
    print(GoldSpot)
    print(PlatinumSpot)


if __name__ == "__main__":
    GetYTSoup()


#  end BS Testing

# YTfeed Functions
# ---------------------------------------------------------------------------------------------------------------------


def FeedMe(request, id):
    f = open('YTnewVideo.html', 'w')
    # the W at the end make the line open and overwrite what there. This ensures that old embeds are not saved.
    YTsubLink = Youtuber.YTlink
    YTfeedHTML = """
    {% extends "YTfeed/YTfeed_base_base.html" %}
    {% load static %}
    {% block title %} {{ name }} {% endblock %}
    {% block content %}
    <html>
    <head>
    </head>
    <body>
    <p>Welcome to YTfeed!!</p>
    <h1 id="NYS">{{YTname}}</h1>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/""" +{}+ """" title="YouTube video player" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>""".format(YTsubLink)
    """
    </body>
    </html>
    <h1 id="NYS">{{YTname}}</h1>
    <a id="list-link" href="{% url 'List-Youtubers' %}"> See Whats New With Your Favorite Youtubers!!!</a>
    {% endblock %}"""
    f.write(YTfeedHTML)
    f.close()
    Youtubers = get_object_or_404(Youtuber, id=id)
    return render(request, "YTfeed/YTfeed_view.html", {
        'Youtuber name': Youtubers.YTname,
        'Latest Video': Youtubers.YTlink,

    })


#  webbrowser.open_new_tab('YTfeed_view.html')


def AddYoutubers(request):
    form = YoutuberForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Add-Youtubers')
    else:
        form = YoutuberForm()
    return render(request, 'YTfeed/YTfeed_add.html', {'form': form})


def EditYoutubers(request, id):
    Youtubers = get_object_or_404(Youtuber, id=id)  # This sets the movie id base on what was chosen by the user.
    form = YoutuberForm(request.POST or None, instance=Youtubers)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/YTfeed/' + id)
    return render(request, "YTfeed/YTfeed_Update.html", {"form": form})


def DeleteYoutubers(request, id):
    Youtubers = get_object_or_404(Youtuber, id=id)
    form = YoutuberForm(request.POST or None, instance=Youtubers)
    if request.method == "POST":
        Youtubers.delete()
        return HttpResponseRedirect('/RidleyVerse/List-Youtubers/')
    return render(request, "RidleyVerse/YTfeed_Delete.html", {"form": form})


def WPgenEDIT(self):
    f = open("WPgenPage.html", "w")
    UserInput = self.UI.get()
    f.write("<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>".format(UserInput))
    f.close()
    fn = 'WPgenPage.html'
    webbrowser.open_new_tab(fn)


# End Modification controls


# ------------------------------------------------------------------------------------------------------------------
#  BackUps       BackUps       BackUps       BackUps       BackUps       BackUps       BackUps       BackUps
# ------------------------------------------------------------------------------------------------------------------


'''
def FeedMe():
    f = open('YTfeedView.html', 'w')
    # the W at the end make the line open and overwrite what there. This ensures that old embeds are not saved.
    YTsubLink = (Youtuber.YTlink("{}".format('YTlink')))
    YTfeedHTML = """<html>
    <head></head>
    <body><p>Welcome to YTfeed!!</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/"""+{}+"""" title="YouTube video player" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>""".format(YTsubLink)
    """
    </html>"""
    f.write(YTfeedHTML)
    f.close()
    webbrowser.open_new_tab('YTfeedView.html')


def YoutuberDetails(request, id):
    Youtubers = get_object_or_404(Youtuber, id=id)
    return render(request, "YTfeed/YTfeed_details.html", {
        'Youtuber name': Youtubers.YTname,
        'Latest Video': Youtubers.YTlink,

    })
    
    
    

# YTfeed Functions


def YTfeedmain(request):
    return render(request, 'RidleyVerse/YTfeed_Main.html')



def FeedMe():
    f = open('YTfeedView.html', 'w')
    # the W at the end make the line open and overwrite what there. This ensures that old embeds are not saved.
    YTsubLink = (Youtuber.YTlink("{}".format('YTlink')))
    YTfeedHTML = """<html>
    <head></head>
    <body><p>Welcome to YTfeed!!</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/"""+{}+"""" title="YouTube video player" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>""".format(YTsubLink);"""
    </html>"""
    f.write(YTfeedHTML)
    f.close()
    webbrowser.open_new_tab('YTfeedView.html')


def DeleteYoutubers(request, id):
    Youtubers = get_object_or_404(Youtuber, id=id)
    form = YoutuberForm(request.POST or None, instance=Youtubers)
    if request.method == "POST":
        Youtubers.delete()
        return HttpResponseRedirect('/RidleyVerse/List-Youtubers/')
    return render(request, "RidleyVerse/YTfeed_Delete.html", {"form": form })


def YoutuberDetails(request, id):
    Youtubers = get_object_or_404(Youtuber, id=id)
    return render(request, "RidleyVerse/YTfeed_details.html", {
        'Youtuber name': Youtuber.YTname,
        'Latest Video': Youtuber.YTlink,

    })




      # This is the WPgen or Web Page Generator function. It uses open() to open/create the HTML file. the w in the function
        # Sets it to overwrite the current text if any. for this function there is no text to start with so the f.write part sets the text for the page
        # I included the tabs and the line breaks that would make the HTML indentation correct for the first function but i found
        # i dident realy need towhen i made the second
    def WPgen(self):
        f = open("WPgenPage.html", "w")
        f.write("<html>\n   <body>\n        <h1>\n  Stay tuned for our amazing summer sale!\n       </h1>\n </body>\n</html>")
        f.close()
        fn = 'WPgenPage.html'
        webbrowser.open_new_tab(fn)

        # This is the WPgenEDIT Web Page Generator Edit function. it functions almos identicly to the WPgen function but it uses self.UI.get() to
        # retreve the text in the self.UI entry field. whatever text is in the feild whent the submit button is clicked is used as the input.
        # With the WPgenPage.html in the same file you can use the filename as is. if it was in a different file you would have to use the file path.
        # I had issues with this at first as i was desegnatinf a file path to the folder i had the PY file in and it was difficult.
    def WPgenEDIT(self):
        f = open("WPgenPage.html", "w")
        UserInput = self.UI.get()
        f.write("<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>".format(UserInput))
        f.close()
        fn = 'WPgenPage.html'
        webbrowser.open_new_tab(fn)

# END YTfeed Functions
'''
