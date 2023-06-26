from django.urls import path
from . import views


urlpatterns = [
    path('', views.shantieshome, name='shanties_home'),
    path('shanties_add/', views.shantiesadd, name='shanties_add'),
    path('shanties_home/', views.shantieshome, name='shanties_home'),
    path('shanties_display/', views.shantiesdisplay, name='shanties_display'),
    path('<int:pk>/shanties_details/', views.shantiesdetails, name='shanties_details')
]
