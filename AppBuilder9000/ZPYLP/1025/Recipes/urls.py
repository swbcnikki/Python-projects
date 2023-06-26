from django.urls import path
from .import views

urlpatterns = [
    path('', views.Recipes_Home, name="Recipes_Home"),
    path('Recipes_Create/', views.Recipes_Create, name="Recipes_Create"),
    path('Recipes_See/', views.Recipes_See, name="Recipes_See"),
    path('Recipes_Details/<int:pk>/', views.Recipes_Details, name="Recipes_Details"),
    path('Recipes_Edit/<int:pk>/', views.Recipes_Edit, name="Recipes_Edit"),
    path('Recipes_Delete/<int:pk>/', views.Recipes_Delete, name="Recipes_Delete"),
    path('Recipes_API/', views.Recipes_SearchAPI, name="Recipes_API"),
]