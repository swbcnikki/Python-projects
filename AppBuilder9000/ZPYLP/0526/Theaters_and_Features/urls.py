from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.Theater_home, name="Theater_home"),
    path('add/', views.new_Theater, name="new_Theater"),
    path('find/', views.find_Theater, name="find_Theater"),
    path('detail/<int:pk>', views.Theater_details, name='Theater_details'),
    path('edit/<int:pk>', views.edit_details, name='edit_details'),
    path('delete/<int:pk>', views.delete_Theater, name='delete_Theater'),
]

