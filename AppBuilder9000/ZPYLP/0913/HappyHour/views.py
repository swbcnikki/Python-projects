from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantsForm
from .models import Restaurants
import requests
import json



def home(request):
#call API from cocktaildb to show recipe for margarita
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    data = requests.get(f)
    tt = json.loads(data.text)
    drinks = tt["drinks"]
    margarita = drinks[0]

    print(margarita['strDrink'])
    print(margarita['strInstructions'])
    context = {'name': margarita['strDrink'], 'instructions': margarita['strInstructions']}



# for i in (tt["drinks"]):
#     print(i["strDrink"], "\n")
#     print(i["strInstructions"], "\n")
#
#     url = i["strDrinkThumb"]




 #get API to show up on home page
    return render(request, 'HappyHour/HH_Home.html', context)



# allows new record to be created and saved to dB
def create_review(request):
    form = RestaurantsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('HH_Create_Review')
    return render(request, 'HappyHour/HH_Create_Review.html', {'form': form})

# displays all records
def list_review(request):
    restaurants= Restaurants.objects.all()
    return render(request, "HappyHour/HH_List.html", {'restaurants': restaurants})

# function allows all data for one record to be viewed and edited
def review_details(request, pk):
    details = Restaurants.objects.get(pk=pk)
    return render(request, "HappyHour/HH_Details.html", {'details': details})


#function allows data to be deleted
def review_delete(request, pk):
    item = get_object_or_404(Restaurants, pk=pk)
    form = RestaurantsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('HH_List')
    return render(request, 'HappyHour/HH_Delete.html', {'item': item, 'form': form})

def review_edit(request, pk):
    item = get_object_or_404(Restaurants, pk=pk)
    form = RestaurantsForm(data=request.POST or None, instance=item)  # selects an instance
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('HH_List')
    content = {'form': form}
    return render(request, 'HappyHour/HH_edit.html', content)