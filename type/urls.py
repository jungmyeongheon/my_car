from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('types/', views.types, name='types'),
    path('types/details/<int:id>', views.details, name='details'),
]