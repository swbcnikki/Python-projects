from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Dallas_home'),
    path('raffle/', views.raffle, name='Dallas_raffle'),
    path('list/', views.DisplayRaffle, name='DisplayRaffle'),
    path('details/<int:pk>', views.RaffleDetails, name='RaffleDetails'),
]