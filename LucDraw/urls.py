# _*_ coding:utf-8 _*_
"""LucDraw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve  #用于处理上传静态文件
from LucDraw.settings import MEDIA_ROOT

from price.views import getform,edit_favorites,favorites

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$', getform, name='go_form'),
    url(r'^edit_favorites/', edit_favorites, name='edit_favorites'),
    url(r'^favorites/', favorites, name='favorites'),

    # 配置上传文件的访问函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
