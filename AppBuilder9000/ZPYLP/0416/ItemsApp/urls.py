from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="itemsApp_home"),
    path('new_item/', views.new_item, name="new_item"),
    path('view_items/', views.display_items, name="display_items"),
    path('details/', views.select_item, name="select_item"),
    path('<int:pk>/details/', views.item_details, name="item_details"),
    path('<int:pk>/edit_form/', views.edit_form, name="edit_items"),
    path('edit_item/', views.edit_page, name="edit_page"),
    path('<int:pk>/delete/', views.delete_item, name="delete"),
    path('confirm_delete/', views.confirm_delete, name="confirm_delete")
]
