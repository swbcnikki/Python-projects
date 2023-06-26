from django.urls import path
from . import views

urlpatterns = [
    path('', views.cocktail_recipes_home, name='cocktail_recipes_home'),
    path('add-cocktail/', views.add_cocktail, name='cocktail_recipes_add_cocktail'),
    path('cocktail-list/', views.cocktail_list, name='cocktail_recipes_cocktail_list'),
    path('<int:pk>/cocktail-detail/', views.cocktail_details, name='cocktail_recipes_details'),
]
