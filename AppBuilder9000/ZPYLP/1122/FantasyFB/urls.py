from django.urls import path

from . import views

urlpatterns = [
    path('', views.fantasyFB_home, name='fantasyFB_home'),
    path('fantasyFB_form/', views.fantasyFB_form, name='fantasyFB_form'),
    path('fantasyFB_roster/', views.fantasyFB_roster, name='fantasyFB_roster'),
    path('<int:pk>/fantasyFB_details', views.fantasyFB_details, name='fantasyFB_details'),
]
