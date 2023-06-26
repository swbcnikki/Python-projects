from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm, JobSearchForm, TestForm
from .forms import CHOICES
import requests
import json
from bs4 import BeautifulSoup


def personality_job_api(request):
    return render(request, 'Personality/personality_job_api.html')


def personality_trait_info(request):
    page = requests.get("https://en.wikipedia.org/wiki/Big_Five_personality_traits")
    soup = BeautifulSoup(page.content, 'html.parser')
    # Scraping general information about the traits
    info = soup.find_all('p')[0].get_text() + soup.find_all('p')[2].get_text()
    openness = soup.find_all('p')[7].get_text()
    conscientiousness = soup.find_all('p')[9].get_text()
    extraversion = soup.find_all('p')[10].get_text() + soup.find_all('p')[11].get_text() + soup.find_all('p')[12].get_text()
    agreeableness = soup.find_all('p')[13].get_text() + soup.find_all('p')[14].get_text() + soup.find_all('p')[15].get_text() + soup.find_all('p')[16].get_text()
    neuroticism = soup.find_all('p')[17].get_text() + soup.find_all('p')[18].get_text() + soup.find_all('p')[19].get_text()
    print(info)
    print(openness)
    print(conscientiousness)
    print(extraversion)
    print(agreeableness)
    print(neuroticism)
    content = {'info': info, 'openness': openness, 'conscientiousness': conscientiousness,
               'extraversion': extraversion, 'agreeableness': agreeableness, 'neuroticism': neuroticism}
    return render(request, 'Personality/personality_trait_info.html', content)


def personality_home(request):
    return render(request, 'Personality/personality_home.html')


def personality_create(request):
    form = PersonForm(data=request.POST or None)
    test = TestForm(data=request.POST or None)
    print("1")
    if request.method == 'POST':
        print("2")
        if form.is_valid():
            print("3")
            if test.is_valid():
                print("4")
                person_instance = form.save(commit=False)
                o_score = 10
                c_score = 10
                e_score = 10
                a_score = 10
                n_score = 10

                o1 = int(test.cleaned_data["questionO1"])
                o2 = int(test.cleaned_data["questionO2"])
                o3 = int(test.cleaned_data["questionO3"])
                o4 = int(test.cleaned_data["questionO4"])
                o5 = int(test.cleaned_data["questionO5"])

                c1 = int(test.cleaned_data["questionC1"])
                c2 = int(test.cleaned_data["questionC2"])
                c3 = int(test.cleaned_data["questionC3"])
                c4 = int(test.cleaned_data["questionC4"])
                c5 = int(test.cleaned_data["questionC5"])

                e1 = int(test.cleaned_data["questionE1"])
                e2 = int(test.cleaned_data["questionE2"])
                e3 = int(test.cleaned_data["questionE3"])
                e4 = int(test.cleaned_data["questionE4"])
                e5 = int(test.cleaned_data["questionE5"])

                a1 = int(test.cleaned_data["questionA1"])
                a2 = int(test.cleaned_data["questionA2"])
                a3 = int(test.cleaned_data["questionA3"])
                a4 = int(test.cleaned_data["questionA4"])
                a5 = int(test.cleaned_data["questionA5"])

                n1 = int(test.cleaned_data["questionN1"])
                n2 = int(test.cleaned_data["questionN2"])
                n3 = int(test.cleaned_data["questionN3"])
                n4 = int(test.cleaned_data["questionN4"])
                n5 = int(test.cleaned_data["questionN5"])

                o_score += o1 + o2 + o3 + o4 + o5
                c_score += c1 + c2 + c3 + c4 + c5
                e_score += e1 + e2 + e3 + e4 + e5
                a_score += a1 + a2 + a3 + a4 + a5
                n_score += n1 + n2 + n3 + n4 + n5

                print('o_score: ' + str(o_score))
                print('c_score: ' + str(c_score))
                print('e_score: ' + str(e_score))
                print('a_score: ' + str(a_score))
                print('n_score: ' + str(n_score))

                o_average = (o_score / 20) * 100
                c_average = (c_score / 20) * 100
                e_average = (e_score / 20) * 100
                a_average = (a_score / 20) * 100
                n_average = (n_score / 20) * 100
                print(o_average)
                print(c_average)
                print(e_average)
                print(a_average)
                print(n_average)
                person_instance.o_average_score = o_average
                person_instance.c_average_score = c_average
                person_instance.e_average_score = e_average
                person_instance.a_average_score = a_average
                person_instance.n_average_score = n_average
                form.save()
                print(person_instance.id)
                url = '../' + str(person_instance.id)
                return redirect(url)
    content = {'form': form, 'test': test}
    return render(request, 'Personality/personality_create.html', content)


def personality_compare(request):
    person = Person.Persons.all()
    content = {"person": person}
    return render(request, 'Personality/personality_compare.html', content)


def personality_details(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = JobSearchForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if person.o_average_score >= person.c_average_score and person.o_average_score >= person.e_average_score and person.o_average_score >= person.a_average_score and person.o_average_score >= person.n_average_score:
                query = 'creative'
            elif person.c_average_score >= person.o_average_score and person.c_average_score >= person.e_average_score and person.c_average_score >= person.a_average_score and person.c_average_score >= person.n_average_score:
                query = 'overtime'
            elif person.e_average_score >= person.c_average_score and person.e_average_score >= person.o_average_score and person.e_average_score >= person.a_average_score and person.e_average_score >= person.n_average_score:
                query = 'social'
            elif person.a_average_score >= person.c_average_score and person.a_average_score >= person.e_average_score and person.a_average_score >= person.o_average_score and person.a_average_score >= person.n_average_score:
                query = 'care'
            elif person.n_average_score >= person.c_average_score and person.n_average_score >= person.e_average_score and person.n_average_score >= person.a_average_score and person.n_average_score >= person.o_average_score:
                query = 'low stress'
            #query = form.cleaned_data['query']
            location = form.cleaned_data['location']

            url = "https://indeed12.p.rapidapi.com/jobs/search"
            headers = {
                'x-rapidapi-host': "indeed12.p.rapidapi.com",
                'x-rapidapi-key': "9afece8438msh5f25fff510a60bbp1954d2jsn7f98f53b6d37"
            }
            parameters = {
                "query": query,
                "location": location
            }
            response = requests.request("GET", url, headers=headers, params=parameters)
            job_info = json.loads(response.text)
            job_url = job_info['indeed_final_url']
            job_list = []
            for job in job_info['hits']:
                job_list.append([job['title'], job['company_name'], job['location']])
            content = {'job_list': job_list, 'job_url': job_url, 'person': person}
            return render(request, 'Personality/personality_job_api.html', content)

    url = "https://image-charts.com/chart?chan=1200%2CeaseInSine&chbr=5&chco=3366FF&chd=t%3A"\
          + str(person.o_average_score) + "%2C" + str(person.c_average_score) + "%2C" + str(person.e_average_score)\
          + "%2C" + str(person.a_average_score) + "%2C" + str(person.n_average_score)\
          + "&chf=b0%2Clg%2C90%2CEA469EFF%2C1%2C03A9F47C%2C0.4&chl=" + str(person.o_average_score)\
          + "%7C" + str(person.c_average_score) + "%7C" + str(person.e_average_score) + "%7C"\
          + str(person.a_average_score) + "%7C" + str(person.n_average_score)\
          + "&chma=50%2C50%2C50%2C50&chs=700x450&cht=bvs&chtt=Big%205%20Personality&chxl=0%3A%7COpenness%7C" \
            "Conscientiousness%7CExtroversion%7CAgreeableness%7CNeuroticism&chxt=x%2Cy"

    content = {'person': person, 'form': form, 'url': url}
    return render(request, 'Personality/personality_details.html', content)


def personality_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(data=request.POST or None, instance=person)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'person': person, 'form': form}
    return render(request, 'Personality/personality_edit.html', content)


def personality_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(data=request.POST or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('../../compare')
    content = {'person': person, 'form': form}
    return render(request, 'Personality/personality_delete.html', content)



