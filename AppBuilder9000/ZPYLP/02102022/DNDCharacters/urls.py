from django.urls import path
from . import views

urlpatterns = [
    path('', views.dnd_characters_home, name='dnd_characters_home'),
    path('', views.dnd_characters_howto, name="dnd_characters_HowTo"),
    path('', views.dnd_characters_classdescript, name="dnd_characters_ClassDescript"),
    path('createCharacter', views.createCharacter, name="createCharacter"),
    path('dnd_character_lookup', views.dnd_character_lookup, name="dnd_character_lookup"),
    path('dnd_character_search', views.dnd_character_search, name="dnd_character_search"),
    path('show_character/<character_id>', views.show_character, name="show_character"),
    path('update_character/<character_id>', views.update_character, name="update_character"),
    path('delete_character/<character_id>', views.delete_character, name="delete_character"),
    path('delete_character/<character_id>', views.delete_character, name="delete_character"),


]