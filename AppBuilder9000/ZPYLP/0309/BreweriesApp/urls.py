from django.urls import path
from . import views

urlpatterns = [
    path('', views.BA_home, name='BA_home'),
    path('addnew/', views.BA_addnew, name='BA_addnew'),
    path('all/', views.BA_index, name='BA_index'),
    path('details/<int:_id>', views.BA_details, name='BA_details'),
    ]