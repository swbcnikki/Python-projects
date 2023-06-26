from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='HipHopReviews_home'),
    path('request', views.request, name='HipHopReviews_request'),
    path('reviews', views.reviews, name='HipHopReviews_reviews'),
    path('artist_details/<int:pk>/', views.artist_details, name='HipHopReviews_details'),
    path('edit/<int:pk>/', views.edit, name='HipHopReviews_edit'),
    path('delete/<int:pk>', views.delete, name='HipHopReviews_delete'),
]