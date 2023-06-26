from django.urls import path
from . import views


urlpatterns = [
    path('', views.heroability_home, name='heroability_home'),
    path('new_hero/', views.heroability_new_hero, name='heroability_new_hero'),
    path('records/', views.heroability_display_all, name='heroability_display_all'),
    path('<int:pk>/details/', views.heroability_details, name='heroability_details'),
    path('<int:pk>/delete_hero/', views.heroability_delete_hero, name='heroability_delete_hero'),
    path('confirm_delete/', views.heroability_confirm_delete, name='heroability_confirm_delete'),
    path('random_heroes/', views.heroability_random_heroes, name='heroability_random_heroes'),

]
