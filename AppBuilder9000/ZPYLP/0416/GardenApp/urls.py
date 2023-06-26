from django.urls import path
from .import views


urlpatterns = [
    path('gardenhome/', views.gardenhome, name='gardenhome'),
    path('gardenplanner/', views.createplanner, name='gardenplanner'),
    path('gardentracker/', views.createtracker, name='gardentracker'),
    path('allvegetables/', views.allvegetables, name='allvegetables'),
    path('<int:pk>/plannerdetails/', views.plannerdetails, name='plannerdetails'),
    path('<int:pk>/planneredit/', views.planneredit, name='planneredit'),
    path('<int:pk>/plannerdelete/', views.plannerdelete, name='plannerdelete'),
    path('<int:pk>/trackerdetails/', views.trackerdetails, name='trackerdetails'),
    path('<int:pk>/trackeredit/', views.trackeredit, name='trackeredit'),
    path('<int:pk>/trackerdelete/', views.trackerdelete, name='trackerdelete')
]