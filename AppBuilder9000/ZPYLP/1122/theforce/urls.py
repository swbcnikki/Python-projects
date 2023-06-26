from django.urls import path
from . import views

urlpatterns = [
       path('', views.The_Force_home, name="_Home"),
       path('Create/', views.The_Force_Create, name="TheForce"),
       path('Event/', views.The_Force_Events, name='Event'),
       path('Edit/<int:pk>/', views.Edit, name='Edit'),
       path('ConfirmDelete/<int:pk>/', views.ConfirmDelete, name='ConfirmDelete'),
       path('Details<int:pk>/', views.The_Force_Details, name='Details'),
]
