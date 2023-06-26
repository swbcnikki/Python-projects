from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.composers, name='composers_home'),
    path('composers_create', views.create_composer, name='composers_create'),
    path('composers_list', views.composers_list, name='composers_list'),
    path('<int:pk>/composers_details', views.composers_details, name='composers_details'),
    path('<int:pk>/composers_edit', views.composers_edit, name='composers_edit'),
    path('<int:pk>/composers_delete', views.composers_delete, name='composers_delete'),
    path('top100_composers', views.composer_scraping, name='top100_composers'),
    path('composers_api', views.oxford_api, name='composers_api'),
]