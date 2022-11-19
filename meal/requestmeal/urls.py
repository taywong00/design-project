from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='meal-home'),
    path('about/', views.about, name='meal-about'),
    path('register/', views.register, name='meal-register'),
    path('menu/', views.menu, name='meal-menu'),
]
