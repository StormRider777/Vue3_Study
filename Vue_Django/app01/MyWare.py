#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :MyWare.py
# @Time      :2022/11/12 23:28
# @Author    :StormRider
from django.middleware.http import MiddlewareMixin
# from django.conf import settings

class MyWare(MiddlewareMixin):
    def process_request(self,request):
        # request.POST.get('csrfmiddlewaretoken','****************')

        # print('=====',request.META)
        # print('+++++',request.POST)

        if request.method=='POST':
            print(request.headers)
            #print('header:',request.META.get('HTTP_X_CSRFTOKEN','******'))


