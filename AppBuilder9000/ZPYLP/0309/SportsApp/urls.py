from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='SportsApp_home'),
    path('add_nba_game/', views.add_nba_game, name='add_nba_game'),
    path('add_fav_player/', views.add_fav_player, name='add_fav_player'),
    path('add_game_archive/', views.add_game_archive, name='add_game_archive'),
    path('add_fav_archive/', views.add_fav_archive, name='add_fav_archive'),
    path('<int:pk>/game_details/', views.game_details, name='game_details'),
    path('<int:pk>/edit_game/', views.edit_game, name='edit_game'),
    path('<int:pk>/delete_game/', views.delete_game, name='delete_game'),
    path('confirm_delete/', views.confirm_delete, name='confirm_delete'),
    path('nba_standings/', views.nba_standings, name='nba_standings'),
]
