from django.urls import path
from . import views


urlpatterns = [
    # imported recipe_home function from views
    path('', views.recipe_home, name='Recipe_Maker'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('list_recipes/', views.list_recipes, name='list_recipes'),
    # an integer pk is passed through the details method
    path('<int:pk>/details/', views.recipe_details, name='recipe_details'),
    path('<int:pk>/update/', views.recipe_update, name='recipe_update'),
    path('<int:pk>/delete_recipe/', views.delete_recipe, name='delete_recipe'),
    path('bsoup/', views.bsoup, name='bsoup'),
]