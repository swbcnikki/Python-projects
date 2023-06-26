from django.urls import path
from . import views

urlpatterns = [
    path('', views.footballstatshome, name='football_stats_home'),
    path('football_create/', views.add_player_stats, name='football_create'),
    path('football_stats/', views.stats, name='football_stats'),
    path('<int:pk>/details/', views.player_details, name='football_stats_details'),
    path('<int:pk>/edit/', views.player_edit, name='football_stats_edit'),
    path('<int:pk>/delete', views.player_delete, name='football_stats_delete'),
    path('history/', views.superbowl_history_scraping, name='football_stats_superbowl_history'),
    path('stats/', views.stats_page, name='football_stats_team_stats'),

#    path('football_ref/', views.web_scraping, name='football_stats_web_scraping'),
#    path('football_search/', views.search, name='football_search'),
    ]