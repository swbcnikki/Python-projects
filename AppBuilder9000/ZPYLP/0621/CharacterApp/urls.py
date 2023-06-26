from django.urls import path
from . import views

urlpatterns = [
    path('', views.Character_home, name="Character_home"),
    path('add', views.Character_add, name="Character_add"),
    path('list_all', views.Character_list, name="Character_list"),
    path('show_all', views.Character_link, name="Character_link"),
    path('Character_details/<int:pk>/', views.Character_details, name="Character_details"),
]