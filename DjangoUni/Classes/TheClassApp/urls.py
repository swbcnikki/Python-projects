
from django.urls import path
from . import views

urlpatterns = [
    path('admin_console', views.admin_console, name='admin_console'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('/createRecord/', views.createRecord, name='createRecord'),
]