from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_home, name='recipes_home'),
    path('create/', views.recipes_create, name='recipes_create'),
    path('display/', views.recipes_display, name='recipes_display'),
    path('<int:pk>/details/', views.recipes_details, name='recipes_details'),
    path('<int:pk>/edit/', views.recipes_edit, name='recipes_edit'),
    path('<int:pk>/delete/', views.recipes_delete, name='recipes_delete'),
    path('import/', views.recipes_import, name='recipes_import'),
]
