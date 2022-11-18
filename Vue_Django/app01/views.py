from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random
from django.middleware.csrf import get_token
# Create your views here.



#@csrf_exempt
def postdata(request):

    print(request.POST.get('name'),request.POST.get('pwd'))
    res={'res':1,'msg':'登录成功','logininfo':request.POST}
    return HttpResponse(json.dumps(res))

def get_csrf_token(request):
    token = get_token(request)
    return HttpResponse(json.dumps({'csrf_token':token}))

def getdata(request):

    s=[
            {'id': '001', 'name': '东方不败','power':15000},
            {'id': '002', 'name': '欧阳千寻', 'power': 1000},
            {'id': '003', 'name': '慕容冷', 'power': 10000},
            {'id': '004', 'name': '诸葛正我', 'power': 15899},
            {'id': '005', 'name': '张飞', 'power': 10230},
            {'id': '006', 'name': '特朗普', 'power': 1000},
            {'id': '007', 'name': '泽连斯基', 'power': 52671},
            {'id': '008', 'name': '俄罗斯联邦', 'power': 11520},
            {'id': '009', 'name': '任我行', 'power': 15822},
            {'id': '010', 'name': '华山七子', 'power': 28802},
        ]
    res=random.choice(s)
    print(res)
    return HttpResponse(json.dumps(res))