#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :MyWare.py
# @Time      :2022/11/25 21:34
# @Author    :StormRider
from django.utils.deprecation import MiddlewareMixin

class MyWare(MiddlewareMixin):
    def process_request(self,request):
        # print('MiddleWare HEADERS:', request.headers)
        # print(request.session)
        pass

    def process_reponse(self,request,response):
        # response.header("Access-Control-Allow-Origin","*")
        #response.header("Access-Control-Allow-Origin", "*") #""http://IPv4:端口");
        # response.setHeader("Access-Control-Allow-Credentials", "true");
        # response.setHeader("Access-Control-Allow-Methods", "GET,POST,PATCH,PUT,OPTIONS,DELETE");
        # response.setHeader("Access-Control-Allow-Headers", "Origin,Content-Type,Cookie,Accept,Token");

        return response
