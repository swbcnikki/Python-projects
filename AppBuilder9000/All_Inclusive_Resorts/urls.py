from django.urls import path
from . import views


urlpatterns = [
    path('', views.resorts_home, name='resorts_home'),
    path('create/', views.resorts_create, name='resorts_create'),
    path('read/', views.resorts_read, name='resorts_read')
]