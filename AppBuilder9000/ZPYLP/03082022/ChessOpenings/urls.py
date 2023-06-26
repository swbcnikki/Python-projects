from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.homepage, name='chess_home'),

    path('chess_search', views.search_games, name="chess_search"),
    path('add_game/', views.add_game, name="add_game"),
    path('<int:pk>/details/', views.game_details, name="game_details"),
    path('<int:pk>/edit/', views.game_edit, name="game_edit"),
    path('<int:pk>/delete/', views.delete, name="game_delete"),
    path('search_api', views.api_search, name="search_api"),
    path('opening_info', views.opening_scrape, name="opening_info")
]
urlpatterns += staticfiles_urlpatterns()
