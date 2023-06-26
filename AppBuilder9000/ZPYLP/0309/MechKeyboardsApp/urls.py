from django.urls import path
from . import views

# urls for different pages on application
urlpatterns = [
    path('', views.home, name='Mech_Keyboards_home'),
    path('create_record/', views.create_record, name='create_record'),
    path('vendor_spotlight/', views.vendor_spotlight, name='vendor_spotlight'),
    path('keyboard_index/', views.keyboard_index, name='keyboard_index'),
    path('search_results/', views.search_results, name='search_results'),
    path('<int:pk>/build_details/', views.build_details, name='build_details'),
    path('<int:pk>/edit_build/', views.edit_build, name='edit_build'),
    path('<int:pk>/delete_build/', views.delete_build, name='delete_build'),
    path('confirm_delete/', views.confirm_delete, name='confirm_delete'),
]
