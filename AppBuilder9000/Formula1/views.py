from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from .forms import ResultForm
from .models import Result

##ADDING IN ALL DATA NEEDED FOR POINT CALCULATIONS

POINTS_PER_POSITION_FEATURE = {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1,
}

POINTS_PER_POSITION_SPRINT = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 3,
    7: 2,
    8: 1,
}

DRIVER_IMAGES = {
    'Alex Albon': 'Formula1/images/drivers/alex.png',
    'Fernando Alonso': 'Formula1/images/drivers/fernando.png',
    'Valterri Bottas': 'Formula1/images/drivers/valtteri.png',
    'Pierre Gasly': 'Formula1/images/drivers/pierre.png',
    'Lewis Hamilton': 'Formula1/images/drivers/lewis.png',
    'Nicholas Latifi': 'Formula1/images/drivers/nicholas.png',
    'Charles Leclerc': 'Formula1/images/drivers/charles.png',
    'Kevin Magnussen': 'Formula1/images/drivers/kevin.png',
    'Lando Norris': 'Formula1/images/drivers/lando.png',
    'Esteban Ocon': 'Formula1/images/drivers/esteban.png',
    'Sergio Perez': 'Formula1/images/drivers/sergio.png',
    'Daniel Ricciardo': 'Formula1/images/drivers/daniel.png',
    'George Russell': 'Formula1/images/drivers/george.png',
    'Carlos Sainz': 'Formula1/images/drivers/carlos.png',
    'Mick Schumacher': 'Formula1/images/drivers/mick.png',
    'Lance Stroll': 'Formula1/images/drivers/lance.png',
    'Yuki Tsunoda': 'Formula1/images/drivers/yuki.png',
    'Max Verstappen': 'Formula1/images/drivers/max.png',
    'Sebastian Vettel': 'Formula1/images/drivers/sebastian.png',
    'Zhou Guanyu': 'Formula1/images/drivers/zhou.png'
}

TEAM_IMAGES = {
    'Alfa Romeo': 'Formula1/images/teams/alfaromeo-big.png',
    'Alpha Tauri': 'Formula1/images/teams/alphatauri.jpg',
    'Alpine': 'Formula1/images/teams/alpine.jpg',
    'Aston Martin': 'Formula1/images/teams/astonmartin.jpg',
    'Ferrari': 'Formula1/images/teams/ferrari.jpg',
    'Haas': 'Formula1/images/teams/haas.jpg',
    'McLaren': 'Formula1/images/teams/mclaren.jpg',
    'Mercedes': 'Formula1/images/teams/mercedes.jpg',
    'Red Bull': 'Formula1/images/teams/redbull.jpg',
    'Williams': 'Formula1/images/teams/williams.jpg'
}

# RENDERS HOME PAGE
def f1_home(request):
    return render(request, "Formula1/Formula1_home.html")

# RENDERS DISPLAY RACE RESULTS PAGE
def race_results(request):
    data = Result.results.all().order_by('Race', 'Race_Type', '-Points_Earned')
    return render(request, "Formula1/Formula1_raceResults.html", {'data': data})

# RENDERS DISPLAY DRIVER RESULTS PAGE
def driver_results(request):
    data = Result.results.all()
    total_points = 0
    driver_tracker = {}
    for result in data:
        if result.Driver_Name not in driver_tracker:
            driver_tracker[result.Driver_Name] = {'team': result.Current_Team, 'total': int(result.Points_Earned)}
        else:
            points = driver_tracker[result.Driver_Name]['total']
            driver_tracker[result.Driver_Name]['total'] = int(result.Points_Earned) + points
    drivers_sorted_list = sorted(driver_tracker.items(), key= lambda x: x[1]['total'], reverse=True)
    drivers_sorted = {}
    for item in drivers_sorted_list:
        drivers_sorted[item[0]] = {list(item[1].keys())[0]:item[1]['team'], list(item[1].keys())[1]:item[1]['total']}

    context = {
        'drivers_sorted': drivers_sorted,
        'total_points': total_points,
        'data': data
    }
    return render(request, "Formula1/Formula1_driverResults.html", context)

# RENDERS DISPLAY TEAM RESULTS PAGE
def team_results(request):
    data = Result.results.all()
    total_points = 0
    team_tracker = {}
    for result in data:
        if result.Current_Team not in team_tracker:
            team_tracker[result.Current_Team] = {'total': int(result.Points_Earned)}
        else:
            points = team_tracker[result.Current_Team]['total']
            team_tracker[result.Current_Team]['total'] = int(result.Points_Earned) + points
    teams_sorted_list = sorted(team_tracker.items(), key= lambda x: x[1]['total'], reverse=True)
    teams_sorted = {}
    for item in teams_sorted_list:
        teams_sorted[item[0]] = {list(item[1].keys())[0]:item[1]['total']}

    context = {
        'teams_sorted': teams_sorted,
        'total_points': total_points,
        'data': data
    }
    return render(request, "Formula1/Formula1_teamResults.html", context)

# RENDERS DRIVER DETAILS PAGE
def driver_details(request, value):
    data = Result.results.all().filter(Driver_Name=value).order_by('Race', 'Race_Type')
    team = data[0].Current_Team
    total = 0
    for result in data:
        total += result.Points_Earned
    img = DRIVER_IMAGES[value]
    summary = [value, team, int(total), img]
    context = {
        'summary': summary,
        'data': data
    }
    return render(request, "Formula1/Formula1_driverDetails.html", context)

# RENDERS TEAM DETAILS PAGE
def team_details(request, value):
    data = Result.results.all().filter(Current_Team=value).order_by('Race', 'Race_Type')
    drivers = []
    races = {}
    total = 0
    for result in data:
        total += result.Points_Earned
        if result.Driver_Name not in drivers:
            drivers.append(result.Driver_Name)
        race_details = [result.Race, result.Race_Type, int(result.Points_Earned)]
        race_specific = "{} - {}".format(result.Race, result.Race_Type)
        if race_specific not in races:
            races[race_specific] = race_details
        else:
            races[race_specific][2] += int(result.Points_Earned)

    img = TEAM_IMAGES[value]
    summary = [value, drivers, int(total), img]
    context = {
        'summary': summary,
        'data': data,
        'races': races
    }
    return render(request, "Formula1/Formula1_teamDetails.html", context)

# RENDERS ADD RESULT PAGE
def add_result(request):
    form = ResultForm()
    return render(request, "Formula1/Formula1_addResult.html", {'form': form})


def edit_result(request, pk):
    obj = get_object_or_404(Result, id=pk)

    form = ResultForm(request.POST or None, instance = obj)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            result = form.save(commit=False)

            # GENERATE DRIVER_RACE_KEY AND ASSIGN IT
            key = f"{result.Race} - {result.Race_Type} - {result.Driver_Name}"
            result.Driver_Race_Key = key
            # USE BUSINESS LOGIC TO CALCULATE POINT TOTAL
            if result.Finishing_Position == 'DNF':
                result.Points_Earned = 0
            else:
                pos = int(result.Finishing_Position)
                if result.Race_Type == 'Feature Race':
                    if pos <= 10:
                        points = POINTS_PER_POSITION_FEATURE[pos]
                        if result.Fastest_Lap == True:
                            points = points + 1
                        result.Points_Earned = points
                    else:
                        result.Points_Earned = 0
                else:
                    if pos <= 8:
                        points = POINTS_PER_POSITION_SPRINT[pos]
                        result.Points_Earned = points
                    else:
                        result.Points_Earned = 0
            try:
                result.save()
                messages.success(request, "Successfully updated the race result.")
                return redirect('race_results')
            except IntegrityError as e:
                messages.error(request, f"{result.Driver_Name} already has a result recorded for {result.Race} - {result.Race_Type}")
                return redirect('edit_result', pk=pk)

        else:
            messages.error(request, "The race result was not updated successfully.")

            context = {'form': form}

            return render(request, "Formula1/Formula1_editResult.html", context)
    else:
        return render(request, "Formula1/Formula1_editResult.html", context)

def delete_result(request, pk):
    result = get_object_or_404(Result, id=pk)
    form = ResultForm(request.POST or None, instance=result)

    context = {'result': result}
    if request.method == 'POST':
        result.delete()

        messages.success(request, "Successfully deleted the race result.")

        return redirect('race_results')

    else:
        return render(request, "Formula1/Formula1_deleteResult.html", context)



# HANDLES FORM DATA FROM ADD RESULT PAGE
def result_submit(request):
    form = ResultForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            result = form.save(commit=False)
            # GENERATE DRIVER_RACE_KEY AND ASSIGN IT
            key = f"{result.Race} - {result.Race_Type} - {result.Driver_Name}"
            result.Driver_Race_Key = key
            # USE BUSINESS LOGIC TO CALCULATE POINT TOTAL
            if result.Finishing_Position == 'DNF':
                result.Points_Earned = 0
            else:
                pos = int(result.Finishing_Position)
                if result.Race_Type == 'Feature Race':
                    if pos <= 10:
                        points = POINTS_PER_POSITION_FEATURE[pos]
                        if result.Fastest_Lap == True:
                            points = points + 1
                        result.Points_Earned = points
                    else:
                        result.Points_Earned = 0
                else:
                    if pos <=8:
                        points = POINTS_PER_POSITION_SPRINT[pos]
                        result.Points_Earned = points
                    else:
                        result.Points_Earned = 0
            ##SAVE ALL DATA TO RESULTS MODEL AND RETURN AN ERROR IF A RESULT HAS ALREADY BEEN RECORDED FOR THAT RACE+DRIVER COMBO
            try:
                result.save()
                messages.success(request, "Result was successfully saved.")
                return redirect('add_result')
            except IntegrityError as e:
                messages.error(request, f"{result.Driver_Name} already has a result recorded for {result.Race} - {result.Race_Type}")
                return redirect('add_result')
        else:
            print(form.errors)
    else:
        messages.error("Error. Result not saved.")
        return redirect('add_result')
