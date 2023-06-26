from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ChefKnives_Home"),
    path('ChefKnives_Create/', views.chefknives_create, name="ChefKnives_Create"),
    path('ChefKnives_View/', views.chefknives_view, name="ChefKnives_View"),
    path('<int:pk>/ChefKnives_Details/', views.chefknives_details, name="ChefKnives_Details"),
    path('<int:pk>/ChefKnives_Edit/', views.chefknives_edit, name="ChefKnives_Edit"),
    path('<int:pk>/ChefKnives_Delete/', views.chefknives_delete, name="ChefKnives_Delete"),
    path('ChefKnives_Soup/', views.chefknives_soup, name="ChefKnives_Soup"),
    path('ChefKnives_Api/', views.chefknives_api, name="ChefKnives_Api"),
]
