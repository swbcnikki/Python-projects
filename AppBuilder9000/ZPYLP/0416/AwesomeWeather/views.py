import requests
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import City, Facts
from .forms import CityForm, FactForm
from django.template import loader


# Create your views here.


def about(request):
    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(request, 'AwesomeWeather/AwesomeWeather_about.html', {'form': form})
    else:
        form = FactForm(None)
    return render(request, 'AwesomeWeather/AwesomeWeather_about.html', {'form': form})


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=84ed84d576a60dbcbf4149fa354c5cfe'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City already exists in the templates!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'AwesomeWeather/AwesomeWeather_home.html', context)  # returns AwesomeWeather_home.html template


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')


def create(request):
    objects = Facts.objects.all()
    context = {'objects': objects}
    return render(request, 'AwesomeWeather/AwesomeWeather_create.html', context)


def weather_details(request, pk):
    facts = get_object_or_404(Facts, pk=pk)
    context = {'facts': facts}
    return render(request, 'AwesomeWeather/AwesomeWeather_details.html', context)








