from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage view
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),

    
 
]
