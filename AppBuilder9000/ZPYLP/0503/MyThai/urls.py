from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyThai_home, name="MyThai_home"),
    path('my_food/', views.my_restaurants_view, name="MyThai_my_restaurants"),
    path('add_restaurant/', views.new_restaurant, name="MyThai_add_restaurant"),
    path('add_dish/', views.new_dish, name="MyThai_add_dish"),
    path('<int:pk>/dish/', views.details, name="MyThai_details"),
    path('<int:pk>/dish/edit/', views.dish_edit, name="MyThai_dish_edit"),
    path('<int:pk>/dish/delete/', views.dish_delete, name="MyThai_dish_delete"),
    path('<int:pk>/restaurant/', views.restaurant_details, name="MyThai_rest_details"),
    path('<int:pk>/restaurant/edit/', views.restaurant_edit, name="MyThai_rest_edit"),
    path('<int:pk>/restaurant/delete/', views.restaurant_delete, name="MyThai_rest_delete"),
    path('dish_deleted', views.dish_confirmed, name="MyThai_dish_confirmed"),
    path('search/', views.restaurant_search, name="MyThai_restaurant_search"),
    path('results/', views.restaurant_results, name="MyThai_results"),
]
