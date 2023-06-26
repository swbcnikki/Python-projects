from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ArtGallery_home'),
    path('ArtGallery_login/', views.apply, name="ArtGallery_login"),
    path('ArtGallery_users/', views.users, name="ArtGallery_users"),
    path('ArtGallery_details/<int:pk>/', views.user_details, name="ArtGallery_details"),
]
