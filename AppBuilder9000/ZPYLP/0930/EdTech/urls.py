from django.urls import path
from . import views

urlpatterns = [
    path('', views.EdTech_Home, name='EdTech_Home'),
    path('EdTech_Create/', views.EdTech_Create, name='EdTech_Create'),
    path('<int:pk>/EdTech_Delete/', views.EdTech_Delete, name="EdTech_Delete"),
    path('<int:pk>/EdTech_Details/',views.EdTech_Details, name='EdTech_Details'),
    path('<int:pk>/EdTech_Edit/', views.EdTech_Edit, name="EdTech_Edit"),
    path('EdTech_Entries/', views.EdTech_Entries, name='EdTech_Entries'),
]