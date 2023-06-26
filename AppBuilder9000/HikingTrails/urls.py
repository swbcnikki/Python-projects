from django.urls import path
from . import views

urlpatterns = [
    path('', views.HikingTrails_home, name='HikingTrails_home'),
    path('HikingTrails_create', views.HikingTrails_create, name='HikingTrails_create'),
    path('HikingTrails_display', views.HikingTrails_display, name='HikingTrails_display'),
    path('<int:pk>/HikingTrails_details', views.HikingTrails_details, name='HikingTrails_details'),
]