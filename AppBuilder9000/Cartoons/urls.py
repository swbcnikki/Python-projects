from django.urls import path
from . import views


urlpatterns = [
    path('', views.Cartoons, name='Cartoons_home'),
    path('create/', views.CreateCartoon, name='Cartoons_create'),
    path('list/', views.DisplayCartoons, name='Cartoons_list'),
    path('details/<int:pk>', views.DisplayDetails, name='Cartoons_details'),
    path('delete/<int:pk>', views.DeleteItem, name="Cartoons_delete"),
    path('up_date/<int:pk>', views.UpdateItem, name="Cartoons_up_date"),
    path('rankings/', views.CartoonScrape, name='Cartoons_rankings'),
    path('movies/', views.MovieScrape, name='Cartoons_movies'),
    path('api', views.OxfordAPI, name='Cartoons_api'),
    path('definitions', views.DisplayDefinitions, name='Cartoons_definitions'),
]