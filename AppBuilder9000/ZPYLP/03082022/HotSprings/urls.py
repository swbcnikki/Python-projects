from django.urls import path
from .import views


urlpatterns = [
    path('', views.hotsprings_home, name='hotsprings_home'),
    path('hotsprings_create/', views.add_hotsprings, name='hotsprings_create'),
    path('hotsprings_list/', views.list_hotsprings, name='hotsprings_list'),
    path('hotsprings_details/<int:pk>', views.hotsprings_details, name='hotsprings_details'),

]
