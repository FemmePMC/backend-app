from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.getRoute),
    path('alert/<str:pk>/', views.getAlert),
    path('alert/create/', views.createAlert),
    path('alert/<str:pk>/delete', views.deleteAlert),
]