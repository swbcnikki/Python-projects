
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    TheClassApp = ['adulting', 'peopling', 'crisis']
    context = {
        'TheClassApp': TheClassApp
    }
    return render(request, 'home.html', context)