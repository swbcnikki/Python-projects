from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='records_home'),
    path('Records_View/', views.records_view, name='records_view'),
    path('Records_Add/', views.records_add, name='records_add'),
    path('Records_Random/', views.records_random, name='records_random'),
    path('<int:pk>/Records_Details/', views.records_details, name='records_details'),
    path('<int:pk>/Records_Edit/', views.records_edit, name='records_edit'),
    path('<int:pk>/Records_Delete/', views.records_delete, name='records_delete'),
]