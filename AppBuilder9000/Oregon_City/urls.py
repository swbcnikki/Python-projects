from django.urls import path
from . import views

urlpatterns = [
    path('', views.oregon_home, name='oregon_home'),
    path('Oregon_create/', views.oregon_create, name='oregon_create'),
    path('display/', views.oregon_display, name='oregon_display'),
    path('<int:pk>/details/', views.oregon_details, name='oregon_details'),
    path('<int:pk>/update/', views.oregon_update, name='oregon_update'),
    path('<int:pk>/delete/', views.oregon_delete, name='oregon_delete'),
    path('api/', views.oregon_api, name='oregon_api'),
]
