from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='WR_home'),
    path('recipes', views.create_recipes, name='WR_create_recipes'),
    path('ViewRecipes', views.view_recipes, name='WR_view_recipes'),
    path('RecipeDetails/<int:id>/', views.recipe_details, name='WR_recipe_details'),

]