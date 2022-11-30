"""meal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('requestmeal/', include('requestmeal.urls')),
    #path('requestmeal/register')
    path('requestmeal/login/', auth_views.LoginView.as_view(template_name = 'requestmeal/login.html'), name = 'login'),
    path('requestmeal/logout/', auth_views.LogoutView.as_view(template_name = 'requestmeal/logout.html'), name = 'logout'),
    path('admin/', admin.site.urls),
]
