from django.urls import path
from . import views

urlpatterns = [
    path('', views.StockMarketHome, name='StockMarketHome'),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction'),
    path('display/', views.display, name='display'),
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('API/', views.API, name='API'),
]
