from django.urls import path
from . import views

# Stores url patterns to determine which Views functions to call
urlpatterns = [
    path('', views.turtles_home, name='turtles_home'),  # Default if there is no path.
    path('create/', views.turtles_create, name='turtles_create'),  # Path to 'turtles_create.html'
    path('display/', views.turtles_display, name='turtles_display'),  # Path to 'turtles_display.html'
    # Calls the 'turtles_details()' function and passes in the pk(primary key).
    path('<int:pk>/turtles_details/', views.turtles_details, name='turtles_details'),
    path('<int:pk>/turtles_edit/', views.turtles_edit, name='turtles_edit'),
    path('<int:pk>/turtles_delete/', views.turtles_delete, name='turtles_delete'),
]
