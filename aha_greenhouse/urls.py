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
from django.views.static import serve
from apps.monitor.views import index

from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitor/', include('monitor.urls'),),  # 环境监测
    path('user/', include('user.urls'),),  # 用户管理
    path('control/', include('controller.urls'), ),  # 用户管理
    path('forum/', include('forum.urls'), ),  # 用户管理
    path('ueditor/', include('DjangoUeditor.urls')),  # 添加DjangoUeditor的URL
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 增加此行
    path('', index, name='index'),  # 环境监测
]
