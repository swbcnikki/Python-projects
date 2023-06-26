from django.urls import path

from Speedster import views

urlpatterns = [
    path('Speedster_home/', views.Speedster_home, name='Speedster_home'),
    path('Speedster_add/', views.Speedster_add, name='Speedster_add'),
    path('Speedster_profile/', views.Speedster_profile, name='Speedster_profile'),
    path('Speedster_database/', views.Speedster_database, name='Speedster_database'),
    path('Speedster_details/<int:id>', views.Speedster_details, name='Speedster_details'),
    path('Speedster_index/', views.Speedster_index, name='Speedster_index'),
]
