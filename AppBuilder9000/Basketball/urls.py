from django.urls import path
from . import views

urlpatterns = [
    path('', views.basketballHome, name='Basketball_Home'),
    path('pickup', views.basketballPickup, name='Pickup_Games'),
    path('search', views.searchPickup, name='Search_Pickup'),
    path('get', views.pickupGameGet, name='Pickup_GameGet'),
    path('details/<int:pk>', views.basketballDetail, name='details'),
    path('edit/<int:pk>', views.basketballEdit, name='edit'),
    path('delete/<int:pk>', views.basketballDelete, name='delete')
]
