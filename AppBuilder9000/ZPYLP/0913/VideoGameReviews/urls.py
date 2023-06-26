from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="gamereviews_home"),
    path('add_review/', views.add_review, name="gamereviews_addreview"),
    path('reviews/', views.view_review, name="gamereviews_displayitems"),
    path('<int:pk>/details/', views.review_details, name="gamereviews_details"),
    path('<int:pk>/edit/', views.review_edit, name="gamereviews_edit"),
    path('<int:pk>/delete/', views.review_delete, name="gamereviews_delete"),
]
