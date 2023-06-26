#story1, step4: Add function to views to render the home page
# add function with name matching urls.py views.xxxx (match xxxx), url will call this function and display something on the screen.

from django.shortcuts import render, redirect, get_object_or_404            # get_object_or_404 = This function calls the given model and get object from that if that object or model doesn’t exist it raise 404 error.
from .models import RvtFunction, User                                       # MUST import classes
from .forms import AddRvtFunctionForm, AddUserForm                          # MUST import forms
import requests
import json



# Create your views here.
def RevitFunctions_home(request):
    return render(request, 'RevitFunctions/RevitFunctions_home.html')

# Story2, step 4: Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
# function for the form: AddRvtFunction
def RevitFunctions_AddRvtFunction(request):
    form = AddRvtFunctionForm(data=request.POST or None)                    # request.POST is referring to the data that comes through when you "post" it from a form.
                                                                                # None is if no data is currently coming through.
                                                                                # does not evaluate to True or False, but returns one of the objects.
                                                                            # POST request sends the information from the form to the server, The server processes the information from the Post request
                                                                                # The server responds by displaying whatever success or failure response it has
                                                                            # When the QueryDict request.POST is empty, it takes a Falsy value, so the item on RHS
                                                                                # of the or operation is selected (which is None), and the form is initialized without
                                                                                # vanilla arguments (i.e. with None): form = MyModelForm()
                                                                                # Otherwise, when request.POST is not empty, the form is initialized with the QueryDict:
                                                                                # form = MyModelForm(request.POST)


    if request.method == 'POST':
        if form.is_valid():
                                                                            # Django’s form is returned using the POST method in which the browser
                                                                                # bundles up the form data, encodes it for transmission, sends it to the server,
                                                                                # and then receives back its response.
                                                                            # form.is_valid() = used to perform validation for each field of the form, it is defined
                                                                                # in Django Form class. It returns True if data is valid and place all data into a
                                                                                # cleaned_data attribute.
            form.save()
            return redirect('RevitFunctions_home')                          # go back to home if true.
    else:
        return render(request, 'RevitFunctions/RevitFunctions_AddRvtFunction.html', {'form': form})
                                                                            # enter form if false.


# Story2, step 4: Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
# function for the form: AddUser
def RevitFunctions_AddUser(request):
    form = AddUserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('RevitFunctions_home')
    else:
        return render(request, 'RevitFunctions/RevitFunctions_AddUser.html', {'form': form})


# Story3, Step2: Add in a function that gets all the items from the database and sends them to the template
# function to see/retrieve all records of RvtFunctions dB
def RevitFunctions_RvtRecords(request):
    rvtrecords = RvtFunction.RvtFunctions.all()                             # check models.py for proper class and object name (class attribute name.variable attributes name)
    return render(request, 'RevitFunctions/RevitFunctions_RvtRecords.html', {'rvtrecords': rvtrecords})


# story4, Step2: Create a views function that will find a single item from the database and send it to the template
# function to see/retrieve details of one item in records by primary key match
def RevitFunctions_RvtDetails(request, pk):
    rvtdetails = get_object_or_404(RvtFunction, pk=pk)                      # check models.py for proper class and object name (class attribute name.variable attributes name)
                                                                            # match the primary key to query that particular item, then assign them into rvtdetails.
    return render(request, 'RevitFunctions/RevitFunctions_RvtDetails.html', {'rvtdetails': rvtdetails})


# Story5, step3: Have the views function send the information for the single item and save any changes.
# function for the form: RvtEdit.html
def RevitFunctions_RvtEdit(request, pk):
    rvtedit = get_object_or_404(RvtFunction, pk=pk)                         # check models.py for proper class and object name (class attribute name.variable attributes name)

    # Use model forms and instances to display the content of a single item from the database
    form = AddRvtFunctionForm(data=request.POST or None, instance=rvtedit)  # instance=rvtedit will populate the cell with the original values.
                                                                            # use the same form as AddRvtFunctionForm
                                                                            # https://stackoverflow.com/questions/4673985/how-to-update-an-object-from-edit-form-in-django
                                                                            # request.POST is referring to the data that comes through when you "post" it from a form.
                                                                                # None is if no data is currently coming through.
                                                                                # does not evaluate to True or False, but returns one of the objects.
                                                                            # When the QueryDict request.POST is empty, it takes a Falsy value, so the item on RHS
                                                                                # of the or operation is selected (which is None), and the form is initialized without
                                                                                # vanilla arguments (i.e. with None): form = MyModelForm()
                                                                                # Otherwise, when request.POST is not empty, the form is initialized with the QueryDict:
                                                                                # form = MyModelForm(request.POST)


    if request.method == 'POST':                                            # if this method='POST', the template must have something referrencing this for it to POST somthing.
        if form.is_valid():
                                                                            # Django’s form is returned using the POST method in which the browser
                                                                                # bundles up the form data, encodes it for transmission, sends it to the server,
                                                                                # and then receives back its response.
                                                                            # form.is_valid() = used to perform validation for each field of the form, it is defined
                                                                                # in Django Form class. It returns True if data is valid and place all data into a
                                                                                # cleaned_data attribute.
            form.save()
            return redirect('RevitFunctions_RvtRecords')                    # go back to home if true.
    else:
        return render(request, 'RevitFunctions/RevitFunctions_RvtEdit.html', {'form': form})
                                                                            # enter form if false.


def RevitFunctions_RvtDelete(request, pk):
    rvtdelete = get_object_or_404(RvtFunction, pk=pk)
    form = AddRvtFunctionForm(request.POST or None, instance=rvtdelete)

    if request.method == 'POST':                                            # if this method='POST', the template must have something referrencing this for it to POST somthing.
        rvtdelete.delete()
        return redirect('RevitFunctions_RvtRecords')

    return render(request, 'RevitFunctions/RevitFunctions_RvtConfirmDelete.html', {'rvtdelete': rvtdelete})

def RevitFunctions_RvtConfirmDelete(request):
    if request.method == 'POST':                                            # if this method='POST', the template must have something referrencing this for it to POST somthing.
        form = AddRvtFunctionForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('RevitFunctions_RvtRecords')
    else:
        return render(request, 'RevitFunctions/RevitFunctions_RvtRecords.html')


# Story6, API pt1 : Only generate the data from terminal, the actual displaying of the results is the next story part.
# utilize google search api instead of building a full database-driven site.
def searchKeywords(request):                                               # this function is to pass in the predefined {{ rvtdetails.google_keywords }} from REvitFuncions_RvtDetails.html
    if request.method == "GET":                                                 # and get JSON to return the search results.
        searchText = request.GET.get("q")                                   # q must match q= in url
        searchText = searchText.replace(' ', '+')                           # replace the space between each words with a plus sign, so it will search all keywords instread of only the first word.
        #print(searchText)                                                  # check in terminal if all searchText shows up.

        #Story6 API pt1, Step3: Connect to the API and write a basic JSON response (either to a txt file or the terminal)
        url = 'https://google-search3.p.rapidapi.com/api/v1/crawl/q={}&num=100&lr=lang_en'.format(searchText)
        #print(url)                                                         # check in terminal if all url results are correct.
                                                                            # q={}central is JSON's way of putting in a wild card
                                                                                # JSON is just a format for transferring data, a collection of Key Value pairs.
                                                                                # get_searchText can be named anything, pass in the get_searchText as the wild card, .get is a built-in function.
                                                                                # original item generated by Google Search API GET CRAWL, when it's non specific: "https://google-search3.p.rapidapi.com/api/v1/crawl/q=revit+save%20local%20+sync%20to%20central=100"
                                                                            # @num=100 should show 100 results (not working on 10/6/21, contacted developer for more info)
                                                                            # &lr=lang_en will show english results
        headers = {
            'x-user-agent': "desktop",
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "9afece8438msh5f25fff510a60bbp1954d2jsn7f98f53b6d37"
            }                                                               # default items generated by Google Search API GET CRAWL: https://rapidapi.com/apigeek/api/google-search3/

        response = requests.request("GET", url, headers=headers)            # default items generated by Google Search API GET CRAWL: https://rapidapi.com/apigeek/api/google-search3/
        response = response.json()                                          # parse python responses to json, allowing json to build a dictionary of the response generated.

        url_title = []
        for key in response['results']:
            url_title.append(key['title'])
        # print(url_title)
        
        url_list = []                                                       # produce dictionary, an array list of key: results and value: link
        for key in response['results']:                                           # format url_list to a template and have it populate in hte RvtDetails page.
            url_list.append(key['link'])
        # print(url_list)                                                     # print to terminal of the url_list, good way to check if the above codes is populating the correct info

        dictionary = {}                                                     # combine both list into a Key: value pair dictionary
        for key in url_title:                                               # key is url_title
            for value in url_list:                                          # value is url_list
                dictionary[key] = value                                     # combine them as one dictionary
                url_list.remove(value)                                      # remove the value the value of url_list, or else only the first url_list will repeat for all keys.
        print(dictionary)


        # for x in url_list:
        #     print(x)
        return render(request, 'RevitFunctions/RevitFunctions_RvtDetails.html', {'dictionary': dictionary})
                                                                            # return to home page after completed, or it will be stuck in this page.
