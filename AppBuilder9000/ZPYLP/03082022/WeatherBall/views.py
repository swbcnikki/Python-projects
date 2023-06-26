from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from .forms import UsersForm
from bs4 import BeautifulSoup
import requests
import json

def weather_home(request):
    return render(request, 'WeatherBall/weatherhome.html')

def weather_create(request):
    form = UsersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('weather_home')
    else:
        print(form.errors)
        form = UsersForm()
    context = {
        'form': form
    }
    return render(request, 'WeatherBall/weathercreate.html', context)

def weather_db(request):
    display = Users.objects.all()
    context = {
        'display': display
    }
    return render(request, 'WeatherBall/weatherdisplaydb.html', context)

def weather_details(request, pk):
    details = get_object_or_404(Users, pk=pk)
    context = {'details': details}
    return render(request, 'WeatherBall/weatherdetails.html', context)

def weather_edit(request, pk):
    edit = get_object_or_404(Users, pk=pk)
    form = UsersForm(data=request.POST or None, instance=edit)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('weather_home')
        else:
            print(form.errors)
            form = UsersForm()
    context = {
        'form': form, 'edit': edit
    }
    return render(request, 'WeatherBall/weatheredit.html', context)

def weather_delete(request, pk):
    item = get_object_or_404(Users, pk=pk)
    form = UsersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('weather_db')
    return render(request, 'WeatherBall/weatherdelete.html', {'item': item, 'form': form})

def weather_scraping(request):
    detailed_forecast = [] #Lists headers of forecast
    weather_body = [] #Lists forecast text for each day
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=35.3434&lon=-90.2983")
    soup = BeautifulSoup(page.content, 'html.parser')
    current = soup.find(id="detailed-forecast-body")
    div_items = current.find_all("div")
    for forecast in div_items:
        bingo = forecast.find_all(class_="forecast-label")
        for i in bingo:
            text = i.get_text()
            detailed_forecast.append(text)
    for content in div_items:
        clouds = content.find_all(class_="forecast-text")
        for rain in clouds:
            message = rain.get_text()
            weather_body.append(message)
    print(detailed_forecast)
    context = {'detailed_forecast': detailed_forecast, 'weather_body': weather_body}
    return render(request, 'WeatherBall/weatherscraping.html', context)

def weather_api(request):
    complete_info = []
    not_complete_info = []
    response = requests.get("https://api.weather.gov/gridpoints/MEG/36,66/forecast")
    sleet = json.loads(response.text)
    wx_properties = sleet['properties']  # this is to go into the properties section of the api
    wx_info = wx_properties['periods']  # we do the same thing with field name seeking forecast
    ''' Here we are doing a for loop to get all of the weather types.
    Made a var assigned as blank string then in for loop we use weather_type to go
    into API and locate the section that has Properties and will then loop through to locate 
    the info in the Periods section. This will loop multiple times to find all results of Periods.
    '''
    for update in wx_info:
        updates = update['name'] #Will give day/s of the week as the result.
        # this is then going to be a var holding our dictionary that is holding the values of the info we got from
        # the above code.
        complete_info.append(updates)
    for i in wx_info:
        temp = i['temperature'] #Will give the daily high and low temperature for the period.
        not_complete_info.append(temp)
      # we then take that info and pass it into our empty list var from the very top
    # and then append the parameter passed in to this to get the string and then use the new info stored inside
    # complete_info and create a for loop in our html to get the info out of it and to be displayed on our api html page.
    print(complete_info)
    print(not_complete_info)
    return render(request, 'WeatherBall/weatherapi.html')
