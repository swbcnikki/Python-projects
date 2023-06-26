from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='WoWApp_home'),
    path('create-character/', views.character_create_view, name='WoWAppCreateCharacter'),
    path('character-list/', views.character_list_view, name='WoWAppCharacterList'),
    path('game-news/', views.game_news_view, name='WoWAppGameNews'),
    path('delete-character/<int:pk>/', views.character_delete_view, name='WoWAppDeleteCharacter'),
    path('character-details/<int:pk>/', views.character_detail_view, name="WoWAppCharacterDetail"),
    path('edit-character/<int:pk>/', views.character_edit_view, name='WoWAppEditCharacter'),
]

