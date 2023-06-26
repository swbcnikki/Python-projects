from django.urls import path
from . import views

urlpatterns = [
    path('', views.Val_home, name='Val_home'),
    path('AddItem/', views.AddItem, name='AddItem'),
    path('Items/', views.Items, name='Items'),
    path('Details/<int:pk>/', views.Details, name='Details'),
    path('Val_edit/<int:pk>/', views.Val_edit, name='Val_edit'),
    path('Val_delete2/<int:pk>/', views.Val_delete2, name='Val_delete2'),
    path('Val_delete_true/', views.Val_delete_true, name='Val_delete_true')
]
