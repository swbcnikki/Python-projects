from django.urls import path
from . import views

urlpatterns = [
    path('', views.florida_birds_home, name='florida_birds_home'),
    path('add-bird/', views.add_bird, name='florida_birds_add_bird'),
    path('display-all-birds/', views.display_all_birds, name='florida_birds_display_all_birds'),
    path('bird-details/<int:pk>/', views.display_details, name='florida_birds_details'),
    path('bird-edit/<int:pk>/', views.edit, name='florida_birds_edit'),
    path('delete_bird/<int:pk>/', views.delete, name='florida_birds_delete'),
    path('api/', views.api, name='florida_birds_api'),
    # path('search-collection', views.search_collection, name='search_collection'),
]
