from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.texmex_home, name='texmex_home'),
    path('view_recipes', views.view_recipes, name="view_recipes"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirmdelete', views.confirmed, name="confirmed"),
    path('createRecord', views.createRecord, name="createRecord"),
    path('recipe_page', views.recipe_page, name="recipe_page")

]