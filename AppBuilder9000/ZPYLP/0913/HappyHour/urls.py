"""HappyHour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='HH_Home'),
    path('add/', views.create_review, name="HH_Create_Review"),
    path('list/', views.list_review, name="HH_List"),
    path('details/<int:pk>', views.review_details, name="HH_Details"),
    path('edit/<int:pk>', views.review_edit, name="HH_Edit"),
    path('delete/<int:pk>', views.review_delete, name="HH_Delete"),
]
