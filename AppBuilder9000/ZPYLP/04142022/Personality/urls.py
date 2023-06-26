from django.urls import path
from . import views

from . import views


#app_name = 'Personality'
urlpatterns = [
    path('', views.personality_home, name='personality_home'),
    path('create/', views.personality_create, name='personality_create'),
    path('compare/', views.personality_compare, name='personality_compare'),
    path('api/', views.personality_job_api, name='personality_job_api'),
    path('info/', views.personality_trait_info, name='personality_trait_info'),
    path('<int:pk>/', views.personality_details, name='personality_details'),
    path('<int:pk>/edit/', views.personality_edit, name='personality_edit'),
    path('<int:pk>/delete/', views.personality_delete, name='personality_delete'),
]