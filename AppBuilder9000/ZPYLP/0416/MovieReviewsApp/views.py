from django.shortcuts import render


def MovieReviewsApp_home(request):
    return render(request, 'MovieReviewsApp/MovieReviewsApp_home.html')