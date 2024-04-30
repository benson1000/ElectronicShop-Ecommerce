from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]
