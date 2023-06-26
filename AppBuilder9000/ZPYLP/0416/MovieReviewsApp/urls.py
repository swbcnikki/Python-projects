from django.urls import path
from .import views

urlpatterns = [
    path('', views.MovieReviewsApp_home, name='MovieReviewsApp_home')
]
