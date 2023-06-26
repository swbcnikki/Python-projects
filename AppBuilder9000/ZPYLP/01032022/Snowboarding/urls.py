from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='Snowboarding_Home'),
    path('New_Ryder/', views.AddNewRyder, name='AddNewRyder'),
    path('Ryders/', views.GetAllRyders, name='Ryders'),
    path('<int:pk>/Ryder_Details/', views.Ryder_Details, name='Ryder_Details'),
    path('<int:pk>/Edit_Ryder/', views.Edit_Ryder, name='Edit_Ryder'),
    path('<int:pk>/Delete_Ryder/', views.Delete_Ryder, name='Delete_Ryder'),

]