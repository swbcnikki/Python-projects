from django.shortcuts import render

# Create your views here.
def todoView(request):
    return render(request, 'gardening_home.html')