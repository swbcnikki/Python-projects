from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_home, name='anime_index'),
    path('create/', views.Anime_create, name='Add_Anime'),
    path('entries/', views.Anime_entries, name='Anime_entries'),
    path('<int:pk>/details/', views.Anime_details, name='Anime_details'),
]
