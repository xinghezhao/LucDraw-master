# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.

class UserMessage(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, default='',verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'联系地址')
    image = models.ImageField(upload_to='image/%Y/%m',default=u"image/default.png", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户信息录入'
        verbose_name_plural = verbose_name #显示复数信息，如果不添加会在用户留言后面加一个s