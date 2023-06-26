from django.urls import path
from . import views


urlpatterns = [
    path('', views.mtb_trails_home, name='mtb_trails_home'),
    path('trails_review/', views.mtb_trails_review, name='mtb_trails_review'),
    path('submitted_review/', views.submitted_review, name='submitted_review'),
    path('existing_reviews/', views.existing_reviews, name='existing_reviews'),
    path('review_details/<int:pk>/', views.review_details, name='review_details'),
    path('edit_or_delete/<int:pk>/', views.edit_or_delete, name='edit_or_delete'),
    path('delete_trail/<int:pk>/', views.delete_trail, name='delete_trail'),
    path('top_mtb/', views.top_mtb, name='top_mtb'),
    path('trail_api/', views.trail_api, name='trail_api'),
]
