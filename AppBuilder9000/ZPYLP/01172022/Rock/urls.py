from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('RocksHome', views.RocksHome, name='RocksHome'),
    path('RockCreate', views.Rock_Create, name='RockCreate'),
    path('HardRock_List', views.HardRock_List, name='HardRock_List'),
    path('<int:pk>/details/', views.details, name="details"),
    path('HardRock_Details', views.HardRock_Details, name='HardRock_Details'),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<confirm_delete/', views.confirmed, name="confirmed"),
]
