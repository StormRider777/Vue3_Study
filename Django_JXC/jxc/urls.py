#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :urls.py
# @Time      :2022/12/16 23:28
# @Author    :StormRider

from django.urls import path
from . import views
from . import Kmviews

app_name='jxc'

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'), #POST
    path('logout/', views.logout, name='logout'), #GET

    path('getuserslist/', views.getuserslist, name='getuserslist'), #GET
    path('adduser/', views.adduser, name='adduser'),  #POST
    path('deleuser/', views.deleuser, name='deleuser'), #POST
    path('updateuser/',views.updateuser,name='updateuser'), #POST
    path('getmyinfo/',views.getmyinfo,name='getmyinfo'), #GET
    path('changepwd/',views.changepwd,name='changepwd'), #POST

    path('addkm/',Kmviews.addKm,name='addkm'), #POST
    path('updatekm/',Kmviews.updateKm,name='updatekm'), #POST
    path('delekm/',Kmviews.deleKm,name='delekm'), #POST
    path('getkm/',Kmviews.getKm,name='getkm'), #GET

]