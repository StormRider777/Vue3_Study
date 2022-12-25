#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :JxcWare.py
# @Time      :2022/12/17 15:32
# @Author    :StormRider

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import json
from . import models

class MyWare(MiddlewareMixin):
    def process_request(self,request):
        expath=[
            'login',
            'logout'
        ]
        if request.session.get('isLogin',False):
            account=request.session.get('account','')
            pwd=request.session.get('pwd','')
            row=models.Users.objects.filter(account=account,pwd=pwd).first()
            if row:
                pass
            else:
                return HttpResponse(json.dumps({'res': 0, 'msg': '非法用户!', 'data': None}))
        else:
            mpath=request.path.split('/')
            if len(mpath)>2:
                mpath=mpath[2]
                if mpath in expath:
                    pass
                else:
                    return HttpResponse(json.dumps({'res':0,'msg':'请确认是否已经登录!','data':None}))
            else:
                return HttpResponse(json.dumps({'res': 0, 'msg': '请登录!', 'data': None}))

    def process_response(self,request,reponse):
        return reponse