# Imports;
from django.urls import path
from . import views

# URL Patterns;
urlpatterns = [
    path('', views.SLS_home, name='StreetLeagueSkateboarding_home'),
    path('StreetLeagueSkateboarding_create/', views.SLS_create, name='StreetLeagueSkateboarding_create'),
    path('StreetLeagueSkateboarding_view/', views.SLS_view, name='StreetLeagueSkateboarding_view'),
    path('<int:pk>/StreetLeagueSkateboarding_details/', views.SLS_details, name='StreetLeagueSkateboarding_details'),
    path('<int:pk>/update/', views.SLS_update, name='StreetLeagueSkateboarding_update'),
    path('<int:pk>/delete/', views.SLS_delete, name='StreetLeagueSkateboarding_delete'),
    path('api/', views.SLS_api, name='StreetLeagueSkateboarding_api'),
    path('<int:m>/save_api/', views.SLS_save_api, name='StreetLeagueSkateboarding_save_api'),
    path('bs/', views.SLS_bs, name='StreetLeagueSkateboarding_bs'),
]