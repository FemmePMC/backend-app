from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoute),
    path('users/', views.getUsers),
    path('user/create/', views.createUser),
    path('user/<str:pk>/update', views.updateUser),
    path('user/<str:pk>/delete', views.deleteUser),
    path('user/<str:pk>/', views.getUser),
    path('user/<str:pk>/patch', views.patchUser),
    path('user/<str:pk>/emergency_contacts/', views.getRelatedUsers),
    path('user/<str:pk>/add/<str:pk2>/', views.relateUser),
    path('user/<str:pk>/alert/<str:pkAlert>/', views.relateAlert),
    path('user/<str:pk>/alerts/', views.getRelatedAlerts),
    path('user/<str:pk>/location/', views.getRelatedLocation),
    path('user/<str:pk>/location/patch/', views.patchRelatedLocation),
    
]