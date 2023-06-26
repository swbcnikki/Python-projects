from django.urls import path, include
from SciFiWatchlist import views

urlpatterns = [
    path('SciFi-home/', views.SciFihome, name='SciFi-Home'),
    path('Add-Movies/', views.AddMovies, name='Add-Movies'),
    path('List-Movies/', views.ListMovies, name='List-Movies'),
    path('<id>', views.MovieDetails, name='Movie-Details'),
    path('<id>/update/', views.EditMovies, name='Update'),
    path('<id>/delete/', views.DeleteMovies, name='Delete')
    ]