from django.shortcuts import render, redirect, get_object_or_404
from .forms import NeighborhoodForm, ReviewForm
from .models import Neighborhood, Review
from django.db.models import Count, F, Value, Avg
import requests
from bs4 import BeautifulSoup
import json



#takes you to homepage.


def neighborhoodReview_home(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['neighborhood_id']
        return reviewpage(request, pk)
    content = {'form': form}
    return render(request, "NeighborhoodReview/NeighborhoodReview_home.html", content)


# creates a neighborhood to be reviewed.


def create_neighborhood(request):
    form = NeighborhoodForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('NeighborhoodReview/NeighborhoodReview_home.html')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/CreateNewNeighborhood.html', content)

# allows you to filter neighborhood and see reviews.


def reviewpage(request, pk):
    neighborhood = get_object_or_404(Neighborhood, pk=pk)
    reviews = Review.Reviews.filter(neighborhood_id=pk)
    form = ReviewForm(data=request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
    content = {'neighborhood_id': neighborhood, 'reviews': reviews}
    return render(request, 'NeighborhoodReview/ReviewPage.html', content)

#this is take you to the page where you can write a review. After review is written you will directed to the
#main to see all reviews for the neighborhood


def review(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
           # pk = request.POST['id']
           # form.save()
            return redirect('NeighborhoodReview/NeighborhoodReview_home.html')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/CreateReview.html', content)

#This method allow creates a query object that returns everything from the Neighborhood module/table


def details(request):
    neigh_list = Neighborhood.objects.all()
    detail_content = {'neigh_list': neigh_list}
    return render(request, 'NeighborhoodReview/DisplayAllNeighborhoods.html', detail_content)


#this method creates a filters out detail on a specific neighborhood based on pk
#it returns all the fields in the neighborhood field as well as the average rating
#for the neighborhood.


def item_details(request, id):

    neigh_item = get_object_or_404(Neighborhood, id=id)
    reviews = Review.Reviews.filter(neighborhood_id=id)
    avg_rating = reviews.aggregate(Avg('rating'))  # creates a dictionary with name rating__avg
    item_content = {'neigh_item': neigh_item, 'avg_rating': avg_rating}
    return render(request, 'NeighborhoodReview/DisplayNeighborhood_item.html', item_content)


def edit_neighborhood(request, pk):
    item = get_object_or_404(Neighborhood, pk=pk)
    form = NeighborhoodForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../neighborhood_item_details')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/edit.html', content)


# deletes neighborhood, then sends you to confirmation page where neighborhood can be perminately deleted.


def delete_neighborhood(request, pk):
    pk = int(pk)
    item = get_object_or_404(Neighborhood, pk=pk)
    form = NeighborhoodForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        item.delete()
        return redirect('NeighborhoodReview/DisplayAllNeighborhoods.html')
    content = {"item": item, "form": form}
    return render(request, 'NeighborhoodReview/DeleteNeighborhood.html', content)


def edit_review(request, id):
    item = get_object_or_404(Review, id=id)
    form = ReviewForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../review_item_detail/')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/edit_review.html', content)


def delete_review(request, id):

    item = get_object_or_404(Review, id=id)
    form = ReviewForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        item.delete()
        return redirect('NeighborhoodReview/Review_Details.html')
    content = {"item": item, "form": form}
    return render(request, 'NeighborhoodReview/DeleteReview.html', content)


#renders an html of all reviews, so that user can select and delete ones deemed "inappropriate"


def review_details(request):
    review_list = Review.Reviews.all()
    content = {'review_list': review_list}
    return render(request, 'NeighborhoodReview/Review_Details.html', content)


def review_item(request, id):

    item = Review.Reviews.filter(id=id)
    get_item = get_object_or_404(item, id=id)
    item_content = {'get_item': get_item}
    return render(request, 'NeighborhoodReview/Review_items.html', item_content)


def soup_page(request):
    page = requests.get("https://smartasset.com/taxes/oregon-property-tax-calculator")
    soup = BeautifulSoup(page.content, 'html.parser')  #connect to page using beautiful soup.
    data = []
    tax_table = soup.find("div", attrs={"id": "table-pk-16840"})  # find the table with the data, locate the class needed
    rows = tax_table.findAll("tr")  # find all elements in tr or below
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]  # iterate through columns and strip extra space
        data.append([ele for ele in cols if ele])  # if the there's an element in the column append to the data.

    data_list = []
    for sublist in data:
        for item in sublist:
            data_list.append(item)  #takes list of list and combines it into a list so it can be formatted neatly.

    county = data_list[::4]  #subsetting data
    value = data_list[1::4] # take every 4th element in the list.
    tax_pymt = data_list[2::4]
    tax_rate = data_list[3::4]
    zipped_list = zip(county, value, tax_pymt, tax_rate) # adding list together, so they can be iterated through.
    content = {'zipped_list': zipped_list}
    return render(request, "NeighborhoodReview/BeautifulSoup.html", content)


def api_pull(request): # if time permits I will be updating this part to add more relevant data.
    data = {}
    if 'id' in request.GET:
        id = request.GET['id']
        url = 'https://api.openbrewerydb.org/breweries/' + str(id) #use str(id) to filter appropriate data.
        response = requests.get(url)
        data = response.json()
    return render(request, 'NeighborhoodReview/API.html', {'data': data})


def api_data(request):
    content ={}
    if 'year' in request.GET:
        year = request.GET['year']
        param ={'year':year}  #user can input year to see how things vary from year to year.
        url = 'https://ruby.datausa.io/api/data?measure=Property Value by Bucket,Property Value by Bucket%20Moe&geo=31000US38900,01000US&drilldowns=Value%20Bucket'
        response = requests.get(url, param)
        data_dict = response.json() # put data into a dict object
        data = data_dict['data']  # remove unnecessary data
        jsonStr = json.dumps(data) # convert data into string
        # parsed_json = (json.loads(jsonStr))
        usableString = str(jsonStr).replace("{", "").replace("}", "")  # remove { so data can be neatly put into list.
        List = list(usableString.split(", "))  # makes it so for ever ", " a new element is add to the index.
        # partition into list with needed data.
        raw_value_bkt = List[235::10]
        raw_bkt_qty = List[238::10]
        raw_year_id = List[236::10]
        # remove the string before the data, so only the data needed is left. (removing the field name from the list)
        value_bkt = []
        for string in raw_value_bkt:
            value_bkt.append(str(string).replace("\"Value Bucket\":", ""))


        bkt_qty = []
        for string in raw_bkt_qty:
            bkt_qty.append(str(string).replace("\"Property Value by Bucket\":", ""))


        year_id = []
        for string in raw_year_id:
            year_id.append(str(string).replace("\"ID Year\":", ""))


        year_id = [space.strip(' ') for space in year_id]  # remove spaces
        bkt_qty = [space.strip(' ') for space in bkt_qty]  # remove spaces
        bkt_qty = [int(string) for string in bkt_qty]  # convert string into integers
        ratio = []
        for num in bkt_qty:
            ratio.append(round(100*num/sum(bkt_qty),3))   # make a field that has ratio of housing market for each bucket


        zipped_data = zip(year_id,value_bkt,bkt_qty,ratio)
        content = {'zipped_data': zipped_data}
    return render(request, "NeighborhoodReview/Metro_Housing_Inventory_Data.html", content)