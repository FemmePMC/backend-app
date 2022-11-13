from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.getRoute),
    path('forums/', views.getForums),
    path('forum/create/', views.createForum),
    path('forum/<str:pk>/update', views.updateForum),
    path('forum/<str:pk>/delete', views.deleteForum),
    path('forum/<str:pk>/', views.getForum),
]