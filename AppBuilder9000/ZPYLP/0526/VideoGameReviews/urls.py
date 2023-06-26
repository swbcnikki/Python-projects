from django.urls import path
from . import views

urlpatterns = [
    path('', views.videogamereviews, name="VideoGamesReview_Home"),
    path('VideoGamesReviews_Reviews/', views.videoreviews, name="VideoGamesReviews_Reviews"),
    path('VideoGamesReviews_Create/', views.create, name="VideoGamesReviews_Create"),
    path('VideoGamesReviews_Details/<int:pk>/', views.videodetails, name="VideoGamesReviews_Details"),
]
