from django.urls import path
from . import views

urlpatterns = [
    path('', views.eft_home, name="eft_items_home"),
    path('create/', views.eft_create_record, name="eft_create_record"),
    path('display_items/', views.eft_all_items, name="eft_all_items"),
    path('details/<int:pk>', views.eft_details, name="eft_item_details"),
    path('edit/<int:pk>', views.eft_edit, name="eft_edit_item"),
    path('delete/<int:pk>', views.eft_delete, name="eft_delete_item"),
    path('EFT_API/', views.eft_api, name="eft_connect_api"),
]
