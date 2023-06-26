from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='AlbumTracker_home'),
    path('details/', views.details, name='AlbumTracker_details'),
    path('add_album/', views.add_album, name='AlbumTracker_add'),
]
