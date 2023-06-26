from django.urls import path
from . import views

urlpatterns = [
    path('', views.stocks_home, name='stocks_home'),
    path('stocks_favorites/', views.favorites, name='stocks_favorites'),
    path('stocks_add_favorites/', views.add_favorites, name='add_favorites'),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirm_delete', views.confirm, name="confirm"),
    path('stocks_news', views.stock_news, name="news"),
]

