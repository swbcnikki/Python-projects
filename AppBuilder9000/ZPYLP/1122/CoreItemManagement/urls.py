# invoking the name while views.'method' page occurs on browser
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cim_home, name="cim_home"),
    path('add/', views.cim_new, name="cim_new"),
    path('edit/', views.cim_edit, name="cim_edit"),
    path('items/', views.cim_list, name="cim_list"),
    path('item/<int:pk>', views.cim_item, name="cim_item"),
    path('addVendor/', views.cim_newVendor, name="cim_newVendor"),
    path('vendors/', views.cim_listVendor, name="cim_listVendor"),
]