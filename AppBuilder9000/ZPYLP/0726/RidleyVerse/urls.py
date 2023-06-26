"""RidleyVerse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from RidleyVerse import views

urlpatterns = [
    path('', views.RidleyVersehome, name='RidleyVerse-home'),
    path('Add-Movies/', views.AddMovies, name='Add-Movies'),
    path('List-Movies/', views.ListMovies, name='List-Movies'),
    path('<id>', views.MovieDetails, name='Movie-Details'),
    path('<id>/update/', views.EditMovies, name='Update'),
    path('<id>/delete/', views.DeleteMovies, name='Delete'),
    path('Full-Story/', views.GetRidleySoup, name='Full-Story')
    ]
