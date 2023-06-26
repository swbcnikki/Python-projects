from django.urls import path
from . import views

urlpatterns = [
    path('', views.TravelDestinationshome, name='TravelDestinations_home'),
    path('TravelDestinations_add/', views.TravelDestinationsadd, name='TravelDestinations_add'),
    path('TravelDestinations_views/', views.TravelDestinationsviews, name='TravelDestinations_views'),
    path('TravelDestinations_detail<int:pk>/', views.TravelDestinationsdetail, name='TravelDestinations_detail')
]