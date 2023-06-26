from django.urls import path
from . import views

# The url patterns that are used within the app
urlpatterns = [
    path('', views.homepage, name="moviereviews_home"),
    path('moviereviews_create/', views.moviereviews_create, name="moviereviews_create"),
    path('moviereviews_display/', views.moviereviews_display, name="moviereviews_display"),
    path('<int:pk>/moviereviews_details/', views.moviereviews_details, name="moviereviews_details"),
    path('<int:pk>/moviereviews_edit/', views.moviereviews_edit, name="moviereviews_edit"),
    path('<int:pk>/moviereviews_delete/', views.moviereviews_delete, name="moviereviews_delete"),
    path('moviereviews_scraping/', views.moviereviews_scraping, name="moviereviews_scraping"),
    path('moviereviews_api/', views.moviereviews_api, name="moviereviews_api"),


]


