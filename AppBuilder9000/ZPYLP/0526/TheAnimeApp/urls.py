from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimeHome, name="AnimeHome"),
    path('AnimeReviews/', views.AnimeReviews, name="AnimeReviews"),
    path('AnimeCreate/', views.AnimeCreate, name="AnimeCreate"),
    path('AnimeDisplay/', views.AnimeDisplay, name='AnimeDisplay'),
    path('AnimeDetails/<int:pk>/', views.AnimeDetails, name='AnimeDetails'),
]
