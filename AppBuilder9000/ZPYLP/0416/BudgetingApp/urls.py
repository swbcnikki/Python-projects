from django.urls import path
from .import views


urlpatterns = [
    path('home', views.home, name='BudgetingApp_home'),
    path('login', views.login, name='BudgetingApp_login'),
    path('budget', views.create_budget, name='BudgetingApp_budget'),
    path('account', views.account, name='BudgetingApp_account'),
    path('details/<int:pk>/', views.details, name='BudgetingApp_details'),
]