from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.f1_home, name="f1_home"),
    path('add_result/', views.add_result, name="add_result"),
    path('race_results/', views.race_results, name="race_results"),
    path('driver_results/', views.driver_results, name="driver_results"),
    path('team_results/', views.team_results, name="team_results"),
    path('edit/result/<int:pk>', views.edit_result, name="edit_result"),
    path('delete/result/<int:pk>', views.delete_result, name="delete_result"),
    path('details/driver/<str:value>/', views.driver_details, name="driver_details"),
    path('details/team/<str:value>/', views.team_details, name="team_details"),
    path('result_submit/', views.result_submit, name="result_submit"),
    path('admin/', admin.site.urls),
]