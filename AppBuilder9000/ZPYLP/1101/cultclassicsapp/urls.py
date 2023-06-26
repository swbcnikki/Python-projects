# invoking the name while views.'method' page occurs on browser
from django.urls import path
from .import views

urlpatterns = [
    path('', views.cultclassicsHome, name="cultclassicsHome"),
    path('CultClassicsCreate/', views.CultClassicsCreate, name='CultClassicsCreate'),
    path('CultClassicsMovies/', views.CultClassicsMovies, name="CultClassicsMovies"),
    path('CultClassicsDetails/<int:pk>/', views.CultClassicsDetails, name="CultClassicsDetails"),
]