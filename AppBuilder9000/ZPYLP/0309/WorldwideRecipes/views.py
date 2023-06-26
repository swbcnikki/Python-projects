from django.shortcuts import render

# Create your views here.


def wwrecipeshome(request):
    return render(request, 'WorldwideRecipes/wwrecipeshome.html')
