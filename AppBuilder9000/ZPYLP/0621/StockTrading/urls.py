from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stories/', views.stories, name='stories'),
    path('about/', views.about, name='about'),
    path('about/story/', views.story, name='story'),
    path('about/resource/', views.resource, name='resource'),
    path('<int:pk>/details/', views.details, name='details'),
]

