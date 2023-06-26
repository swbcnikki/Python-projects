from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.motorcycling_home, name="motorcycling_home"),
    path('rate_motorcycle/', views.create_motorcycle, name="rate_motorcycle"),
    path('rate_route/', views.create_route, name="rate_route"),
    path('list_motorcycles/', views.all_motorcycles, name="list_motorcycles"),
    path('admin_console/', views.admin_console, name="admin_console"),
    path('list_routes/', views.all_routes, name="list_routes"),
    path('<int:pk>/motorcycle_details/', views.motorcycle_details, name="motorcycle_details"),
    path('<int:pk>/route_details/', views.route_details, name="route_detail"),
    path('<int:pk>/update_motorcycle/', views.update_motorcycle, name="update_motorcycle"),
    path('<int:pk>/delete_motorcycle/', views.delete_motorcycle, name="delete_motorcycle"),
    path('<int:pk>/update_route/', views.update_route, name="update_route"),
    path('<int:pk>/delete_route/', views.delete_route, name="delete_route"),
    path('motorcycling_scraper/', views.BS_scraper, name="BS_scraper"),
    path('motorcycling_API/', views.motorcycling_API, name="motorcycling_API"),
]

