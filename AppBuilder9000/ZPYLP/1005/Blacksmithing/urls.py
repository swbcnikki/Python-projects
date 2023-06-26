from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blacksmithing_Home, name='Blacksmithing_Home'),
    path('ToolCreate/', views.Tool_Create, name='Tool_Create'),
    path('ViewTools/', views.View_Tools, name='Tool_View'),
    path('<int:pk>/details/', views.Tool_Details, name='Tool_Details'),
    path('<int:pk>/edit/', views.Edit_Tools, name='Edit_Tools'),
    path('<int:pk>/delete/', views.Delete_Tools, name='Delete_Tools'),
]
