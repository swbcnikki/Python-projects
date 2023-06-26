#story1: step5: create urls.py for your app and homepage
    # urls.py specifies which view is called for a given URL pattern.
    # prior to this is 4. templates
    # urls py maps URLs to the  apps' views.
    # mapping is done through pairs of: Regular expression or a view in a Django app.



from django.urls import path
from . import views                                   # this use the views py from it's mainapp


# request sent to switchboard, and it comes to here, then url will say what to do.
# UrlPatterns list = [ 'pattern to watch for', the function to call, "shortcut name"]
# [ 'commands it's looking for', involk the response, or what should show on user's screen]
# path (this is what shows up after 127.0.0.1:800/xxxxx, function to call, shortname)

urlpatterns = [
    path('', views.RevitFunctions_home, name='RevitFunctions_home'),
                                                # regular expressions, type in xxx.x.x.x:xxxx/admin/ & will see admin.site.urls (if mainApp has admin, there should be no admin in in individual apps such as here).
                                                # add URL for the html page, views.xxxx will call the function in views.py.
                                                # only views.home should not have any location. rest should enter what follows http://127.0.0.1:8000/xxxx/
    path('RevitFunctions_AddRvtFunction/', views.RevitFunctions_AddRvtFunction, name='RevitFunctions_AddRvtFunction'),
    path('RevitFunctions_AddUser/', views.RevitFunctions_AddUser, name='RevitFunctions_AddUser'),

    path('RevitFunctions_RvtRecords/', views.RevitFunctions_RvtRecords, name='RevitFunctions_RvtRecords'),

    # use primary key to display the Balance Sheet (pairing)
    # can be '/RevitFunctions_RvtDetails/<int:pk>/'
    path('<int:pk>/RevitFunctions_RvtDetails/', views.RevitFunctions_RvtDetails, name='RevitFunctions_RvtDetails'),
                                                # Variables within a GET request are usually sent either as part of the headers or as part of the url request.
                                                    # Within Django we use url requests and url patterns for these variables.

    #Story5, Step2: Use model forms and instances to display the content of a single item from the database
    path('<int:pk>/RevitFunctions_RvtEdit/', views.RevitFunctions_RvtEdit, name='RevitFunctions_RvtEdit'),

    path('<int:pk>/RevitFunctions_RvtDelete/', views.RevitFunctions_RvtDelete, name='RevitFunctions_RvtDelete'),
    path('RevitFunctions_RvtConfirmDelete/', views.RevitFunctions_RvtConfirmDelete, name='RevitFunctions_RvtConfirmDelete'),

    #Story6 pt1 API: so a new page generate from this url
    path('GoogleSearchAPI/', views.searchKeywords, name='searchKeywords'),
                                                # can name 'GoogleSearchAPI anything, this is what appears after http://127.0.0.1:8000/xxxx/

]

