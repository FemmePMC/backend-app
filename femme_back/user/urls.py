from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoute),
    path('nombres/', views.getUsers),
    path('nombre/create/', views.createUser),
    path('nombre/<str:pk>/update', views.updateUser),
    path('nombre/<str:pk>/delete', views.deleteUser),
    path('nombre/<str:pk>/', views.getUser),
    
]