from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_reviews_home, name='music_reviews_home'),
    path('Create/', views.createReview, name='createReview'),
    path('review_view/', views.review_view, name='review_view'),
    path('back_home/', views.back_home, name='back_home'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('confirmDelete/', views.confirmDelete, name='confirmDelete'),
    path('<int:pk>/display_reviews/', views.display_reviews, name='display_reviews'),
    path('<int:pk>/editReview/', views.editReview, name='editReview'),
    path('beautiful_soup/', views.beautiful_soup, name='beautiful_soup'),
    path('apiLoad/', views.apiLoad, name='apiLoad'),

]
