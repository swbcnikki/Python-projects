from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_Home, name='stats_Home'),
    path('addPlayer/', views.add_player, name='add_player'),
    path('Players/', views.view_player, name='view_player'),
    path('<int:pk>/Details/', views.view_details, name='view_details'),
]
