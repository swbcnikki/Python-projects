from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardGames_home, name='BoardGames_home'),
    path('create/', views.BoardGames_create, name='BoardGames_create'),
    path('seed/', views.BoardGames_seed, name='BoardGames_seed'),
    path('<int:pk>/details/', views.BoardGames_get, name='BoardGames_get'),
    path('<int:pk>/edit/', views.BoardGames_edit, name='BoardGames_edit'),
    path('<int:pk>/delete/', views.BoardGames_delete, name='BoardGames_delete'),
    path('<int:pk>/favorite/', views.BoardGames_favorite, name="BoardGames_favorite")
]
