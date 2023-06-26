from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kettleBells, name='KB_home'),
    path('get_moves', views.get_moves, name='KB_moves'),
    path('kettleBells_create', views.add_exercise, name='KB_add'),
    path('show_moves/<int:pk>', views.show_moves, name='KB_details'),
    path('kettleBells_edit/<int:pk>', views.kettleBells_edit, name='KB_edit'),
    path('delete_move/<int:pk>', views.delete_move, name='KB_delete'),
]