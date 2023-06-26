from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='basketball_stats_home'),
    path('add_player/', views.create_player, name='basketball_stats_create'),
    path('players/', views.player_stats, name='basketball_stats_players'),
    path('<int:pk>/details/', views.player_details, name='basketball_stats_details'),
    path('<int:pk>/edit/', views.player_edit, name='basketball_stats_edit'),
    path('<int:pk>/delete/', views.player_delete, name='basketball_stats_delete'),
    path('standings/', views.standings_page, name='basketball_stats_standings'),
    path('history/', views.history_scraping, name='basketball_stats_history'),
    path('bball_ref/', views.web_scraping, name='basketball_stats_web_scraping'),
    path('conferences_and_divisions/', views.conference_division, name='basketball_stats_bdl_api'),
    path('save_favorites/', views.save_favorites, name='basketball_stats_save_favorites'),
    path('favorite_teams/', views.view_favorites, name='basketball_stats_favorites'),
    path('<int:pk>/favorite_details/', views.favorite_team_details, name='basketball_stats_favorite_details'),
    path('<int:pk>/delete_favorites/', views.team_delete, name='basketball_stats_delete_favorites'),
]
