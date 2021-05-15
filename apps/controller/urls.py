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
from apps.controller.views import change_status, device_control, control_plan, create_plan, control_history


app_name = 'control'
urlpatterns = [
    path('change_status/', change_status, name='change_status'),
    path('device_control/', device_control, name='device_control'),
    path('control_plan/', control_plan, name='control_plan'),
    path('device_control/create_plan/', create_plan, name='create_plan'),
    path('control_history/', control_history, name='control_history'),
]


