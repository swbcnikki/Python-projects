from django.urls import path
from . import views

urlpatterns = [
    path('', views.SportsCars_Home, name='SportsCars_Home'),
    path('AddSportsCar/', views.AddNewCar, name='AddSportsCar'),
    path('Supercars/', views.Supercars, name='Supercars'),
    path('CarDetails/<int:pk>', views.CarDetails, name = 'CarDetails'),
]