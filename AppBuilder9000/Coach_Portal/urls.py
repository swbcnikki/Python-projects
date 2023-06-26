from django.urls import path
from . import views

urlpatterns = [
    path('', views.coachHome, name='coachHome'),
    path('create/', views.coachCreate, name='coachCreate'),
    path('signups/', views.childCreate, name='coachChildCreate'),
    path('fullroster/', views.childRoster, name='coachChildRoster'),
    path('childdetails/<int:pk>', views.childDetails, name='coachChildDetails'),
    path('childupdate/<int:pk>', views.childUpdate, name='coachChildUpdate'),
    path('childdelete/<int:pk>', views.childDelete, name='coachChildDelete'),
    path('fieldlist/', views.fieldSoup, name='fieldList'),


]