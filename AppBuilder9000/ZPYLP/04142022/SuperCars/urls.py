from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.SuperCarsHome, name='SuperCars_Home'),
    # path('<int:pk>/details/', views.details, name="details"),
    path('CreateRecord/', views.CreateRecord, name='CreateRecord'),
    path('SuperCarsDisplay/', views.SuperCarsDisplay, name='SuperCars_Display'),
    path('<int:pk>/SuperCarsDetails/', views.SuperCarsDetails, name='SuperCars_Details'),

]