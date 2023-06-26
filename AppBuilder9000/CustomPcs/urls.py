from django.urls import path
from . import views
from .views import CreateEntry

urlpatterns = [
    path('', views.CustomPcs_home, name='CustomPcs_Home'),
    path('create/', views.CreateEntry, name='BuildForm'),

]
