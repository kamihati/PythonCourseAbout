# coding=utf8
from django.urls import path

# 导入当前app下的views文件
from . import views

urlpatterns = [
    # 默认页面为views文件中的index
    path('', views.index, name='index'),
    path('i2/', views.index2, name='i3'),
    path('update/', views.update),
    path('slow/', views.slow)
]
