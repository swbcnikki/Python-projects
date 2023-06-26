from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='SW_Home'),
    path('SW_AddProduct', views.SW_AddProduct, name='SW_AddProduct'),
    path('SW_store', views.SW_store, name='SW_store'),
    path('SW_Details/<int:pk>/', views.SW_Details, name="SW_Details"),

]