from django.urls import path
from .views import ClientListCreate, ClientDetail

urlpatterns = [
    path('', ClientListCreate.as_view(), name='client-list'),
    path('<int:pk>/', ClientDetail.as_view(), name='client-detail'),
]
