from django.urls import path
from .import views

urlpatterns = [
    path('', views.pokeDexHome, name='PokeDex_home'),
    path('addPokemon/', views.addPokemon, name='Add_Pokemon_to_PokeDex'),
    path('show_pokemon/', views.show_pokemon, name="show_pokemon"),
    path('<int:pk>/pokemonDetails/', views.pokemon_details, name="pokemon_details"),
    path('<int:pk>/PokeDex_edit/', views.edit_pokemon, name='PokeDex_edit'),
    path('<int:pk>/PokeDex_delete/', views.delete_pokemon, name='PokeDex_delete'),
    path('PokeDex_search/', views.pokeDex_search, name='PokeDex_search'),
    path('PokeDex_api/', views.more_info, name='more_info'),
]