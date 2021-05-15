"""aha_greenhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from apps.user.views import register, log_in, index, log_out, userinfo, reset_password

app_name = 'user'
urlpatterns = [
    path('register', register, name='register'),
    path('login', log_in, name='login'),
    path('index', index, name='index'),
    path('logout', log_out, name='logout'),
    path('userinfo', userinfo, name='userinfo'),
    path('reset_password', reset_password, name='reset_password'),
    path('', index, name='password'),
]


