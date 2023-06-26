from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AlbumReviews_home, name="AlbumReviews_home"),
    path('add/', views.AlbumReviews_add, name="AlbumReviews_add"),
    path('list/', views.AlbumReviews_list, name="AlbumReviews_list"),
    path('details/<int:id>', views.Album_details, name="AlbumReviews_details"),
    path('delete/<int:id>', views.Album_delete, name='AlbumReviews_delete'),
    path('edit/<int:id>', views.Album_edit, name='AlbumReviews_edit'),
]