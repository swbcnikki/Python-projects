from django.urls import include, path
from . import views
from rest_framework import routers
from .views import PetViewSet


router = routers.DefaultRouter()
router.register(r'pet', PetViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.pet_adoption_home, name='pet_adoption_home'),
    path('list/', views.pet_adoption_list, name='pet_adoption_list'),
    path('dogs/', views.pet_adoption_dogs, name='pet_adoption_dogs'),
    path('cats/', views.pet_adoption_cats, name='pet_adoption_cats'),
    path('other/', views.pet_adoption_other, name='pet_adoption_other'),
    path('all/', views.pet_adoption_all, name='pet_adoption_all'),
    path('<int:pk>/details/', views.pet_adoption_details, name='pet_adoption_details'),
    path('<int:pk>/edit/', views.pet_adoption_edit, name='pet_adoption_edit'),
    path('<int:pk>/delete/', views.pet_adoption_delete, name='pet_adoption_delete'),
    path('statistics/', views.pet_adoption_statistics, name='pet_adoption_statistics'),
    path('portland/', views.pet_adoption_portland, name='pet_adoption_portland'),
    path('add/<str:animal>/', views.pet_adoption_add, name='pet_adoption_add'),
    path('search/', views.pet_adoption_search, name='pet_adoption_search'),
]
