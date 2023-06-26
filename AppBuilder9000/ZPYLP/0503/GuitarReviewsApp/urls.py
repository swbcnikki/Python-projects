from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='GuitarReviews_home'),
    path('create', views.create, name='GuitarReviews_create'),
    path('reviews', views.review, name='GuitarReviews_reviews'),
    path('details/<int:pk>/', views.details, name='GuitarReviews_details'),
]
