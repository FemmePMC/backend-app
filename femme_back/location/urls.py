from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.getRoute),
    path('user/location/create/', views.createUbicacion),
    path('user/location/<str:pk>/delete', views.deleteUbicacion),
    path('user/location/<str:pk>/', views.getUbicacion),
]