from django.shortcuts import render,HttpResponse
from django.middleware.csrf import get_token
import random
import json
from . import App01Form
from . import models
from django.db.models import Q,F
# Create your views here.
def index(request):
    return render(request,'app01/index.html')

def gettoken(request):
    token=get_token(request)
    return HttpResponse(token)

def getdata(request):

    data=[
        {'id': '001', 'name': '东方不败', 'salary': random.randint(10000,99999)},
        {'id': '002', 'name': '欧阳锋', 'salary': random.randint(10000,99999)},
        {'id': '003', 'name': '黄老邪', 'salary': random.randint(10000,99999)},
        {'id': '004', 'name': '洪七公', 'salary': random.randint(10000,99999)},
        {'id': '005', 'name': '张三丰', 'salary': random.randint(10000,99999)},
        {'id': '006', 'name': '岳不群', 'salary': random.randint(10000,99999)},
        {'id': '007', 'name': '玄冥二老', 'salary': random.randint(10000,99999)},
        {'id': '008', 'name': '赵敏', 'salary': random.randint(10000,99999)},
        {'id': '009', 'name': '张无忌', 'salary': random.randint(10000,99999)},
        {'id': '010', 'name': '扫地僧', 'salary': random.randint(10000,99999)},
        {'id': '011', 'name': '韦一笑', 'salary': random.randint(10000,99999)},
        {'id': '012', 'name': '郭靖', 'salary': random.randint(10000,99999)},
    ]
    mid=request.GET.get('id', '')
    if not mid:
        res=random.choice(data)
        res = {'res': 1, 'msg': f'随机找到了一条: id={mid} 的数据', 'row': res}
    else:
        findr=False
        for r in data:
            if r['id']==mid:
                res = {'res': 1, 'msg': f'成功找到了: id={mid} 的数据', 'row': r}
                findr=True
                break
        if not findr:
            res={'res':0,'msg':f'没有找到: id={mid} 的数据','row':{}}
    print(res)
    return HttpResponse(json.dumps(res))

def postdata(request):
    print(request.POST)
    if request.POST:
        r={'res':1,'msg':'收到了POST数据!','data':request.POST}
    else:
        r = {'res': 0, 'msg': '没有POST数据!', 'data': request.POST}
    return HttpResponse(json.dumps(r))

def reguser(request):
    if request.method=='GET':
        form=App01Form.UserRegForm()
        return render(request,'app01/reguser.html',context={'form':form})
    else:
        data=request.POST
        photo=request.FILES
        form=App01Form.UserRegForm(data=data,files=photo)
        if form.is_valid():
            form.save()
            return HttpResponse('OK!')
        else:
            return render(request, 'app01/reguser.html', context={'form': form})

def listusers(request):
    data=models.User.objects.all()
    return render(request,'app01/listusers.html',context={'users':data})

def login(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        pwd=request.POST.get('pwd','')
        print('======:',request.POST)
        res=models.User.objects.filter(name=name,pwd=pwd).first()
        if res:
            user={'res':1,'msg':'登录成功!','result':{'name':res.name,'pwd':res.pwd,'tele':res.tele}}
        else:
            user = user={'res':0,'msg':'登录失败:用户名或密码错误!请重试!','result':{'name':'','pwd':'','tele':''}}
        return HttpResponse(json.dumps(user))
    else:
        return HttpResponse('系统登录')

def getmenudata(request):
    menudata={
        
    }

def getyzdata(request):
    if request.method=='GET':
        querykw=request.GET.get('querykw','').strip()
        if not querykw:
            res=list(models.Yz.objects.all().values('id','name','tele','cardid','gzdw'))
        else:
            res = list(models.Yz.objects.filter(
                    Q(name__icontains=querykw) |
                    Q(gzdw__icontains=querykw) |
                    Q(cardid__icontains=querykw) |
                    Q(tele__icontains=querykw)
            ).values('id', 'name', 'tele', 'cardid', 'gzdw'))

        return HttpResponse(json.dumps(res))
    else:
        data=request.POST
        if data.get('type','')=='':
            try:
                name=data['name']
                tele = data['tele']
                cardid = data['cardid']
                gzdw = data['gzdw']
                models.Yz.objects.filter(id=data['id']).update(name=name,tele=tele,cardid=cardid,gzdw=gzdw)
                res = {'res': 1, 'msg': name+'  '+tele+'修改成功!','data':data}
            except Exception as e:
                res = {'res': 0, 'msg': '更新失败:'+repr(e)}

            return HttpResponse(json.dumps(res))
        elif data.get('type','')=='add':
            name = data['name']
            tele = data['tele']
            cardid = data['cardid']
            gzdw = data['gzdw']
            try:
                models.Yz.objects.create(name=name,tele=tele,cardid=cardid,gzdw=gzdw)
                res = {'res': 1, 'msg': '增加业务记录成功', 'data': data}
            except Exception as e:
                res = {'res': 0, 'msg': '增加业务记录失败', 'data': data}

            return HttpResponse(json.dumps(res))
        elif data.get('type','')=='dele':
            id=data.get('id','')
            try:
                models.Yz.objects.filter(id=int(id)).delete()
                res = {'res': 1, 'msg': '删除成功!', 'data': data}
            except Exception as e:
                res = {'res': 0, 'msg': '删除失败!'+repr(e), 'data': data}
            return HttpResponse(json.dumps(res))