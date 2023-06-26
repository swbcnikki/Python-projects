from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="gamestats_home"),
    path('add_game', views.add_game, name="gamestats_form"),
    path('view_games', views.view_games, name="gamestats_viewall"),
    path('<int:pk>/details/', views.game_details, name="gamestats_one"),
    path('<int:pk>/edit/', views.game_edit, name="gamestats_edit"),
    path('<int:pk>/delete/', views.game_delete, name="gamestats_delete"),
    path('topgames', views.top_games, name="gamestats_topgames"),
    path('topgames/<int:id>/', views.top_game_one, name="gamestats_topgame_one"),
    path('apilist', views.api_game_view, name="gamestats_explore"),
    path('add_favorite', views.add_favorite_page, name="gamestats_add_favorite"),
    path('favorites', views.view_favorites, name="gamestats_view_favorites"),
    path('deletefavorite/', views.favorite_delete, name="gamestats_delete_favorite"),
]