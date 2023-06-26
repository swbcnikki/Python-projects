from django.urls import path
from . import views

# urls for different pages on application
urlpatterns = [
    path('', views.home, name='MetalGearApp_Home'),
    path('create/', views.create, name='create'),
    path('index/', views.index, name='index'),
    path('<int:pk>/dogDetails/', views.dogDetails, name='dogDetails'),
]