from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HikingApp_home, name='HikingApp_home'),
    path('AddTrail/', views.create_trail, name="HikingApp_addtrail"),
    path('Index/', views.display_index, name='HikingApp_index'),
    path('Search/', views.search_results, name='HikingApp_searchresults'),
    path('<int:pk>/Details', views.trail_details, name='HikingApp_details'),
    path('<int:pk>/Edit', views.edit_trail, name='HikingApp_edit'),
    path('<int:pk>/delete/', views.delete_trail, name='HikingApp_delete'),
]