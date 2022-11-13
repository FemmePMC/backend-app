from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.getRoute),
    path('nombre/ubicacion/create/', views.createUbicacion),
    path('nombre/ubicacion/<str:pk>/delete', views.deleteUbicacion),
    path('nombre/ubicacion/<str:pk>/', views.getUbicacion),
]