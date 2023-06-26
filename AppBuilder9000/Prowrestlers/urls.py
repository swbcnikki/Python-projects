from django.urls import path
from . import views

urlpatterns = [
    path('', views.wrestlers_home, name='wrestlers_home'),
    path('ProWrestling_createpage/', views.add_prowrestler, name='wrestlers_create'),
    path('<int:pk>/ProWrestling_details/', views.prowrestler_details, name='wrestlers_details'),
    path('ProWrestling_views/', views.prowrestler_views, name='wrestlers_views'),
]