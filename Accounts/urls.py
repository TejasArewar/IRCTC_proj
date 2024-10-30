from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login,name='login'),
    path('profile/', views.profile,name='profile'),
    path('logout/', views.logout,name='logout'),
]
