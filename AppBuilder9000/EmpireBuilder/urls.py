
from django.contrib import admin

from django.urls import path
from . import views

urlpatterns =[
    path('', views.eb_home, name='eb_home'),
    path('reserve/', views.eb_reserve, name='eb_reservation'),
    path('stations/', views.eb_stations, name='eb_stations'),
    path('accommodations/', views.eb_accommodations, name='eb_accommodations'),
    path('gallery/', views.eb_gallery, name='eb_gallery'),
    path('created/', views.eb_created, name='eb_created'),
    path('<int:pk>/details/', views.eb_details, name='eb_details'),
    path('cancel/', views.eb_cancel, name='eb_cancel'),
    path('<int:pk>/edit/', views.eb_edit, name='eb_edit'),
    path('<int:pk>/delete/', views.eb_delete, name='eb_delete'),
    # path('api/', views.eb_api, name='eb_api'),

]

