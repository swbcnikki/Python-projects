from django.urls import path, include
from . import views
from .views import MusicAlbums_home

urlpatterns = [
    path('', views.MusicAlbums_home, name='MusicAlbums_home'),
    path('Add', views.MusicAlbums_add, name='MusicAlbums_add'),
    path('Display', views.MusicAlbums_display, name='MusicAlbums_display'),
    path('Details/<int:pk>/', views.MusicAlbums_details, name='MusicAlbums_details'),

]