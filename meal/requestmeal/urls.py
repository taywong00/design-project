from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='meal-home'),
    path('about/', views.about, name='meal-about'),
    path('register/', views.register, name='meal-register'),
    path('menu/', views.menu, name='meal-menu'),
    path('profile/', views.profile, name='meal-profile'),
    path('adminpage/', views.adminpage, name='meal-adminpage'),
    path('list/', views.list, name='meal-list'),
    path('claim/', views.claim, name='meal-claim'),
    path('requestlist/', views.requestlist, name='meal-requestlist'),
    path('studentlist/', views.studentlist, name='meal-studentlist'),
]
