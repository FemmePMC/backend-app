from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoute),
    path('nombres/', views.getNombres),
    path('nombres/create/', views.createNombre),
    path('nombres/<str:pk>/update', views.updateNombre),
    path('nombres/<str:pk>/delete', views.deleteNombre),
    path('nombres/<str:pk>/', views.getNombre),
    
]