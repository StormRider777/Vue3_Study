from django.shortcuts import render,HttpResponse
from django.db.models import Q,F
from . import models
from . import mm
import json
import datetime
# Create your views here.
import decimal

class DateTimeEncoder(json.JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.strftime()
        if isinstance(obj,decimal.Decimal):
            return float(obj)

def index(request):
    return render(request,'jxc/index.html')

'''
# 用户登录 保存 session
# url:/jxc/login 
# method: POST data:  {account, pwd}
'''
def login(request):
    if request.method=='POST':
        account=request.POST.get('account','')
        pwd=request.POST.get('pwd','')
        # print(request.POST)
        # mm.md5mm(pwd) -前端传送来的密码已是加密后端密码,使用该pwd即可,无需再加密
        row=models.Users.objects.filter(account=account,pwd=pwd).first()
        request.session.set_expiry(0)
        request.session['isLogin'] = False
        request.session['username'] = ''
        request.session['pwd'] = ''
        request.session['account'] = ''
        if row:
            request.session.set_expiry(60*60*24*100)
            request.session['isLogin']=True
            request.session['username']=row.name
            request.session['pwd']=pwd
            request.session['account']=account
            res={'res':1,'msg':'登录成功:','data':{'name':row.name,'account':account,'pwd':row.pwd,'islogin':True}}
        else:
            res = {'res': 0, 'msg': '登录失败:用户名或密码错误', 'data': {'name': '', 'account': '','pwd':''}}
    else:
        res = {'res': 0, 'msg': '登录失败:请求失败!', 'data': {'name': '', 'account': '','pwd':''}}

    return HttpResponse(json.dumps(res,default=str))

'''
# 用户退出系统 保存 session
# url:/jxc/logout 
# method: GET data:  {account, pwd}
'''
def logout(request):
    if request.method=='GET':
        request.session.flush()
        res={'res':1,'msg':'系统退出:','data':None}
    else:
        res = {'res': 0, 'msg': '登录失败:请求失败!', 'data': None}

    return HttpResponse(json.dumps(res,default=str))

'''
# 获取用户列表
# url:/jxc/getuserslists/?kw=xxxxx
# method: GET
'''
def getuserslist(request):
    if request.method=='GET':
        kw=request.GET.get('kw','')
        if (kw):
            rows=models.Users.objects.filter(Q(name__icontains=kw)|Q(account__icontains=kw)).all()
        else:
            rows=models.Users.objects.all()
        rows=rows.order_by('-createtime').values('id', 'account', 'name', 'pwd', 'tele', 'photo','createtime')
        rows=list(rows)
        if rows:
            res={'res':1,'msg':'获取成功:','data':rows}
        else:
            res = {'res': 0, 'msg': '没有获取到数据', 'data':[]}
    else:
        res = {'res': 0, 'msg': '获取数据失败:请求失败!', 'data': []}
    return HttpResponse(json.dumps(res,default=str))

'''
# 增加用户
# url:/jxc/adduser  
# method:POST [name,pwd,repwd,account,tele,photo,FILES]
'''
def adduser(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        pwd = request.POST.get('pwd', '')
        account = request.POST.get('account', '')
        tele = request.POST.get('tele', '')
        photof =request.FILES.get('photo','')
        if photof:
            imgfile=savephoto(photof)
        else:
            imgfile=''
        try:
            row=models.Users.objects.create(name=name,
                                        pwd=pwd,
                                        account=account,
                                        tele=tele,
                                        photo=imgfile)
            res = {'res': 1, 'msg': '注册用户成功' , 'data': { 'id':row.id,
                                                        'name':row.name,
                                                         'account':row.account,
                                                         'tele':row.tele,
                                                         'pwd':row.pwd,
                                                         'createtime':row.createtime,
                                                         'photo':row.photo}}
        except Exception as e:
            res={'res':0,'msg':'注册用户失败:'+repr(e),'data':None}
    else:
        res = {'res': 0, 'msg': '请求错误!', 'data': None}
    return HttpResponse(json.dumps(res,default=str))

'''    
# 删除用户
# url:/jxc/deleuser/  
# method:POST [account]
'''
def deleuser(request):
    if request.method=='POST':
        kw=request.POST.get('account','')
        if kw=='0000' or kw=='0001' or kw.upper()=='ADMIN':
            res = {'res': 0, 'msg': f'账号: {kw} 不可以删除!', 'data': None}
        else:
            row=models.Users.objects.filter(account=kw).first()
            if row:
                try:
                    row.delete()
                    res = {'res': 1, 'msg': '删除成功, 账号:'+kw,'data':{'name':row.name,'account':row.account,'tele':row.tele}}
                except Exception as e:
                    res = {'res': 0, 'msg': '删除失败, 账号:' + kw+repr(e),'data':None}
            else:
                res = {'res': 0, 'msg': '删除失败, 账号不存在:' + kw,'data':None}

    else:
        res = {'res': 0, 'msg': '请求错误!', 'data': None}
    return HttpResponse(json.dumps(res))

'''    
# 修改用户
# url:/jxc/updateuser  
# method:POST [account]
'''
def updateuser(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        account = request.POST.get('account', '')
        tele = request.POST.get('tele', '')
        photof = request.FILES.get('photo', '')
        if photof:
            imgfile = savephoto(photof)
        else:
            imgfile = ''
        try:
            models.Users.objects.filter(account=account).update(name=name,
                                        pwd=pwd,
                                        tele=tele,
                                        photo=imgfile)
            res = {'res': 1, 'msg': '修改用户成功', 'data': {'name': name, 'account': account, 'tele': tele}}
        except Exception as e:
            res = {'res': 0, 'msg': '修改用户失败:' + repr(e), 'data': None}
    else:
        res = {'res': 0, 'msg': '请求错误!', 'data': None}
    return HttpResponse(json.dumps(res, default=str))

'''
#
# url:/getmyinfo/ ?kw=xxxx
# method :GET  kw
#
'''
def getmyinfo(request):
    if request.method=='GET':
        kw=request.GET.get('kw','')
        row=models.Users.objects.filter(account=kw).first()
        # print(row)
        if row:
            data={
                'name':row.name,
                'account':row.account,
                'tele':row.tele,
                'photo':row.photo,
                'pwd':row.pwd,
                'createtime':row.createtime
            }
            res = {'res': 1, 'msg': '查询到记录', 'data': data}
        else:
            res = {'res': 0, 'msg': '没有找到账号为: '+kw+' 的记录.', 'data':None}
    else:
        res = {'res': 0, 'msg': '请求错误!error', 'data': None}
    return HttpResponse(json.dumps(res, default=str))

'''
#
# url:/changepwd/ ?account=xxxx
# method :POST  account
#
'''
def changepwd(request):
    if request.method=='POST':
        account=request.POST.get('account','')
        newpwd=request.POST.get('newpwd','')
        oldpwd = request.POST.get('oldpwd', '')

        row=models.Users.objects.filter(account=account,pwd=oldpwd)
        try:
            if row:
                row.update(pwd=newpwd)
                res= {'res':1,'msg':'密码修改成功','data':{}}
            else:
                res = {'res': 0, 'msg': '密码错误,或不存在用户', 'data': {}}
        except Exception as e:
            res = {'res': 0, 'msg': '出现错误:'+repr(e), 'data': {}}
    else:
        res = {'res': 0, 'msg': '请求错误!', 'data': {}}
    return HttpResponse(json.dumps(res))


#保存头像模块
def savephoto(imgfile):
    imgfilename='default.jpg'
    return imgfilename


