from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='swu_home'),
    path('sources', views.sources, name='swu_sources'),
    path('characters', views.characters, name='swu_characters'),
    path('characters_list', views.characters_list, name='characters_list'),
    path('<id>', views.character_details, name='character_details'),
    path('<id>/edit_char_list/', views.edit_char_list, name='edit_char_list'),
    path('<id>/delete_character/', views.delete_character, name='delete_character'),
]
