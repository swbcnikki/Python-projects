from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='yoga_home'),
    path('create', views.create, name="yoga_create"),
    path('items', views.items, name="yoga_items"),
    path('details/<int:pk>', views.details, name="yoga_details"),
]