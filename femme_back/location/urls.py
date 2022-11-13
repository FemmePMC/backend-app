from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.getRoute),
    path('ubicacion/create/', views.createUbicacion),
    path('ubicacion/<str:pk>/delete', views.deleteUbicacion),
    path('ubicacion/<str:pk>/', views.getUbicacion),
]