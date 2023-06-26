from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cars,name='Carhome'),
    path('CarsCreate', views.CarCreate,name='CarCreate'),
    path('CarEntries', views.CarsEntries,name='CarsEntries'),
    path('CarDetails/<int:pk>/', views.CarsDetails,name='CarsDetails'),
    path('CarsView', views.CarsView,name='CarsView'),

]