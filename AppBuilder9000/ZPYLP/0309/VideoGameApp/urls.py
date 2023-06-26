from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.VG_home, name='VideoGameAppHome'),
    path('Game_Details', views.videoGames_add, name='GameDetails'),
    path('Display_Data', views.Display_Games, name='DisplayData'),
    path('data/<int:_id>', views.Retrieve_DetailView, name='SingleItem'),
    path('data/<int:_id>/update', views.UpdateView, name='UpdateView'),
    path('data/<int:_id>/delete', views.DeleteView, name='DeleteView'),

]
