from django.urls import path
from . import views


urlpatterns = [

    path('', views.CarPartsApp_home, name='CarPartsApp_home'),
    path('CarPartsApp_AddPart', views.CarPartsApp_AddPart, name='CarPartsApp_AddPart'),
    path('CarPartsApp_myParts', views.CarPartsApp_myParts, name='CarPartsApp_myParts'),
    path('CarPartsApp_index', views.CarPartsApp_index, name='CarPartsApp_index'),
    path('CarPartsApp_details/<int:pk>', views.CarPartsApp_details, name='CarPartsApp_details'),
    path('CarPartsApp_edit/<int:pk>', views.CarPartsApp_edit, name='CarPartsApp_edit'),
    path('CarPartsApp_delete/<int:pk>', views.CarPartsApp_delete, name='CarPartsApp_delete'),
    path('CarPartsApp_confirmedDelete', views.CarPartsApp_confirmedDelete, name='CarPartsApp_confirmedDelete'),
]
