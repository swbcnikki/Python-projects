from django.urls import path
from . import views

urlpatterns = [
    path('', views.Atv_home, name='Atv_home'),
    path('AtvTrails_create/', views.add_trail, name='add_trail'),
    path('AtvTrails_list/', views.list_trails, name='list_trails'),
    path('<int:pk>/AtvTrails_details/', views.trail_details, name='trail_details'),
    path('<int:pk>/AtvTrails_edit/', views.trail_edit, name='trail_edit'),
    path('<int:pk>/AtvTrails_delete/', views.trail_delete, name='trail_delete'),
    path('AtvTrails_bs/', views.trail_scrape, name='trail_scrape'),
]
