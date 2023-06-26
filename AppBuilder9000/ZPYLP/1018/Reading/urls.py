from django.urls import path
from . import views

urlpatterns=[
    path('', views.Reading_Home, name='Reading_Home'),
    path('Reading_Create/', views.Reading_Create, name='Reading_Create'),
    path('Reading_Records/', views.Reading_Records, name='Reading_Records'),
    path('<int:pk>/Reading_Details/', views.Reading_Details, name='Reading_Details'),
]