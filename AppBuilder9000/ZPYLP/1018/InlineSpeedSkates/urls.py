from django.urls import path
from . import views

# Maps URL path expressions to Python functions (views.py)
urlpatterns = [
    path('', views.InlineSpeedSkates_Home, name='InlineSpeedSkates_Home'),
    path('Review_Create/', views.Review_Create, name='Review_Create'),
    path('Review_Display/', views.Review_Display, name='Review_Display'),
    path('<int:pk>/Review_Details/', views.Review_Details, name='Review_Details'),
]