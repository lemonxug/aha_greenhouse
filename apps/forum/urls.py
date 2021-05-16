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
from apps.forum.views import index, show, tag, list, new_article


app_name = 'forum'
urlpatterns = [
    path('', index, name='index'),
    path('show-<int:sid>.html/', show, name='show'),
    path('tag/<tag>', tag, name='tags'),  # 标签列表页
    path('list-<int:lid>.html', list, name='list'),  # 列表页

    # path('new_article/', new_article, name='new_article'),
]


