#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :urls.py
# @Time      :2022/12/10 19:11
# @Author    :StormRider
from django.urls import path
from . import views

app_name='app01'

urlpatterns=[
    path('',views.index,name='index'),
    path('getdata/',views.getdata,name='getdata'),
    path('postdata/',views.postdata,name='postdata'),
    path('getalldata/',views.getalldata,name='getalldata'),
    path('uploadimg/',views.uploadimg,name='uploadimg'),
    path('getimgs/',views.getimglist,name='getimglist'),
    path('deleimg/',views.deleimg,name='deleimg')

]