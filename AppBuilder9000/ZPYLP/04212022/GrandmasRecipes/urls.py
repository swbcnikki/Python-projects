from django.urls import path
from . import views

# the directory of . is our current directory
# so the above says import views.py from the current directory
# ANATOMY OF A URL ROUTE:
# ('pattern to watch for',method to call,"shortcut name")
# uses "name= " to link in document.

urlpatterns = [
    path('', views.grandmas_home, name='GrandmasRecipes_home'),  # usable link to home page
    path('create', views.grandmas_create, name='GrandmasRecipes_create'),  # usable link to create page
    path('cookbook', views.grandmas_cookbook, name='GrandmasRecipes_cookbook'),  # usable link to cookbook page
    path('<int:pk>/details', views.grandmas_details, name='GrandmasRecipes_details'),  # link 2detail page need:<int:pk>
    path('<int:pk>/edit', views.grandmas_edit, name='GrandmasRecipes_edit'),  # link 2edit page need:<int:pk>
    path('<int:pk>/delete', views.grandma_delete, name='GrandmasRecipes_delete'),  # link 2delete page need:<int:pk>
]
