from django.shortcuts import render,HttpResponse
from django.middleware.csrf import get_token
import random
import json
import os
# Create your views here.

def index(request):
    request.session['name']='Jack'
    request.session['pwd']='1234'
    return render(request,'app01/index.html')

def getalldata(request):
    data = [
        {'id': '001', 'name': '东方不败', 'salary': random.randint(10000, 99999)},
        {'id': '002', 'name': '欧阳锋', 'salary': random.randint(10000, 99999)},
        {'id': '003', 'name': '黄老邪', 'salary': random.randint(10000, 99999)},
        {'id': '004', 'name': '洪七公', 'salary': random.randint(10000, 99999)},
        {'id': '005', 'name': '张三丰', 'salary': random.randint(10000, 99999)},
        {'id': '006', 'name': '岳不群', 'salary': random.randint(10000, 99999)},
        {'id': '007', 'name': '玄冥二老', 'salary': random.randint(10000, 99999)},
        {'id': '008', 'name': '赵敏', 'salary': random.randint(10000, 99999)},
        {'id': '009', 'name': '张无忌', 'salary': random.randint(10000, 99999)},
        {'id': '010', 'name': '扫地僧', 'salary': random.randint(10000, 99999)},
        {'id': '011', 'name': '韦一笑', 'salary': random.randint(10000, 99999)},
        {'id': '012', 'name': '郭靖', 'salary': random.randint(10000, 99999)},
        {'id': '013', 'name': '岳灵珊', 'salary': random.randint(10000, 99999)},
        {'id': '014', 'name': '韦小宝', 'salary': random.randint(10000, 99999)},
        {'id': '015', 'name': '成吉思汗', 'salary': random.randint(10000, 99999)},
        {'id': '016', 'name': '风清扬', 'salary': random.randint(10000, 99999)},
        {'id': '017', 'name': '任盈盈', 'salary': random.randint(10000, 99999)},
        {'id': '018', 'name': '朱元璋', 'salary': random.randint(10000, 99999)},
        {'id': '019', 'name': '穆念慈', 'salary': random.randint(10000, 99999)},
    ]
    return HttpResponse(json.dumps(data))

def getdata(request):
    data=[
        {'id': '001', 'name': '东方不败', 'salary': random.randint(10000, 99999)},
        {'id': '002', 'name': '欧阳锋', 'salary': random.randint(10000, 99999)},
        {'id': '003', 'name': '黄老邪', 'salary': random.randint(10000, 99999)},
        {'id': '004', 'name': '洪七公', 'salary': random.randint(10000, 99999)},
        {'id': '005', 'name': '张三丰', 'salary': random.randint(10000, 99999)},
        {'id': '006', 'name': '岳不群', 'salary': random.randint(10000, 99999)},
        {'id': '007', 'name': '玄冥二老', 'salary': random.randint(10000, 99999)},
        {'id': '008', 'name': '赵敏', 'salary': random.randint(10000, 99999)},
        {'id': '009', 'name': '张无忌', 'salary': random.randint(10000, 99999)},
        {'id': '010', 'name': '扫地僧', 'salary': random.randint(10000, 99999)},
        {'id': '011', 'name': '韦一笑', 'salary': random.randint(10000, 99999)},
        {'id': '012', 'name': '郭靖', 'salary': random.randint(10000, 99999)},
        {'id': '013', 'name': '岳灵珊', 'salary': random.randint(10000, 99999)},
        {'id': '014', 'name': '韦小宝', 'salary': random.randint(10000, 99999)},
        {'id': '015', 'name': '成吉思汗', 'salary': random.randint(10000, 99999)},
        {'id': '016', 'name': '风清扬', 'salary': random.randint(10000, 99999)},
        {'id': '017', 'name': '任盈盈', 'salary': random.randint(10000, 99999)},
        {'id': '018', 'name': '朱元璋', 'salary': random.randint(10000, 99999)},
        {'id': '019', 'name': '穆念慈', 'salary': random.randint(10000, 99999)},
    ]
    request.session['csrftoken']=get_token(request)
    res=random.choice(data)
    return HttpResponse(json.dumps(res))

def postdata(request):
    data=request.POST
    print(data)
    res={'res':1,'msg':'已收到: POST 数据 成功','data':data}
    return HttpResponse(json.dumps(res))

def uploadimg(request):
    mfile=request.FILES.get('file',None)
    # print(os.getcwd())
    # print(mfile,mfile.name,mfile.size,mfile.content_type)
    if mfile:
        tfile=os.path.join('app01','static','app01','upload',mfile.name)
        with open(tfile,'wb') as f:
            for c in mfile.chunks():
                f.write(c)
        return HttpResponse('ok')
    else:
        return HttpResponse('No File Found!')

def getimglist(request):
    imgpath=os.path.join('app01','static','app01','upload')
    files=os.listdir(imgpath)
    if files:
        return HttpResponse(json.dumps(files))
    else:
        return HttpResponse(json.dumps(None))

def deleimg(request):
    mdelef=request.GET.get('fname','')
    fpath=os.path.join('app01','static','app01','upload',mdelef)
    print(mdelef)
    if os.path.isfile(fpath) and mdelef:
        try:
            os.remove(fpath)
            res={'res':1,'msg':'文件:'+mdelef+':已删除!'}
        except Exception as e:
            res = {'res': 0, 'msg': repr(e)}
    else:
        res = {'res': 0, 'msg': '文件:' + mdelef + ':不存在!'}
    return HttpResponse(json.dumps(res))

