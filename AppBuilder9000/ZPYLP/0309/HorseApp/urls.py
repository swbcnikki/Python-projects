from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='HorseApp_Home'),
    path('HorseApp_Add_Horse/', views.addhorse, name='HorseApp_Add_Horse'),
    path('HorseApp_Index/', views.horseindex, name='HorseApp_Index'),
]
