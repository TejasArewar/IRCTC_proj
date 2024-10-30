from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trains/', views.trains, name='trains'),
    path('available_train/', views.available_train, name='available_train'),
    path('book/<int:id>/', views.book, name='book'),
]