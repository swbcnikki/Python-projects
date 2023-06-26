from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ArtistsApp_home'),
    path('ArtistsApp_creator', views.ArtistsApp_creator, name='ArtistsApp_creator'),
    path('ArtistsApp_index', views.index, name='ArtistsApp_index'),
    path('<int:pk>/ArtistsApp_details', views.ArtistsApp_details, name='ArtistsApp_details'),

]



