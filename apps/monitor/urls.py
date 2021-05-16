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
from apps.monitor.views import index, detail, get_data, query_environmentdata, add_data, analysis


app_name = 'monitor'
urlpatterns = [
    path('', index, name='index'),   # 监控首页
    path('<int:house_id>/', detail, name='detail'),  # 大棚详情页
    path('<int:house_id>/get_data/', get_data, name='get_data'),   # 获取实时数据
    path('query/environment_data/', query_environmentdata, name='environment_data'),  # 查询环境数据
    path('add_data/', add_data, name='add_data'),  # 数据接口
    path('analysis/', analysis, name='analysis'),  # 折线图
]


