from . import views
from django.urls import path

urlpatterns = [
    path('', views.coffee_home, name="coffee_home"),
    path('drink_menu', views.drink_menu, name="drink_menu"),
    path('current_drinks', views.current_drinks, name= "current_drinks"),
]
