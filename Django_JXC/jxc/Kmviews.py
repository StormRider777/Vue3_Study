#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :Kmviews.py
# @Time      :2022/12/22 22:02
# @Author    :StormRider
from django.shortcuts import render,HttpResponse
import json
from . import models

'''
# 增加科目
path('addkm/', Kmviews.addKm, name='addkm'),  # POST
data: kmmc,kmbm,kmxz,pid
'''
def addKm(request):
    if request.method=='POST':
        pid = request.POST.get('pid', '')
        kmmc=request.POST.get('kmmc','')
        kmbm=request.POST.get('kmbm','')
        kmxz=request.POST.get('kmxz','')
        qcsl = request.POST.get('qcsl', '')
        qcje = request.POST.get('qcje', '')
        zbqy=request.POST.get('zbqy', False)
        if int(pid):
            pid=int(pid)
        else:
            pid=None
        try:
            data=models.Kmb.objects.create(_parentId=pid,kmbm=kmbm,kmmc=kmmc,kmxz=int(kmxz),qcsl=qcsl,qcje=qcje,zbqy=zbqy)
            res={'res':1,'msg':'成功添加',
                 'data':{'id': data.id, '_parentId': data._parentId, 'kmbm': data.kmbm,'kmmc':data.kmmc,
                         'label': data.kmbm+' '+data.kmmc,
                         'qcsl':data.qcsl,'qcje':data.qcje,'zbqy':data.zbqy}}
        except Exception as e:
            res = {'res': 0, 'msg': '添加失败:'+repr(e), 'data': None}
    else:
        res = {'res': 0, 'msg': '请求错误!','data': None}
    return HttpResponse(json.dumps(res,default=str))

'''
# 修改科目
path('updatekm/', Kmviews.updateKm, name='updatekm'),  # POST
'''
def updateKm(request):
    if request.method=='POST':
        id = int(request.POST .get('id', '-1'))
        pid=request.POST.get('pid',None)

        kmmc=request.POST.get('kmmc','')
        kmbm=request.POST.get('kmbm','')
        kmxz=request.POST.get('kmxz','')
        qcsl = request.POST.get('qcsl', '')
        qcje = request.POST.get('qcje', '')
        zbqy=request.POST.get('zbqy', '')
        if zbqy=='true':
            zbqy=True
        else:
            zbqy=False

        if pid:
            pid=int(pid)
        print(id,zbqy,type(zbqy))
        try:
            models.Kmb.objects.filter(id=id).update(kmmc=kmmc,kmxz=kmxz,qcsl=qcsl,qcje=qcje,zbqy=zbqy)
            res = {'res': 1, 'msg': '成功添加',
                   'data': {'id': id, '_parentId': pid, 'kmbm': kmbm, 'kmmc': kmmc,
                            'label': kmbm + ' ' + kmmc,
                            'qcsl': qcsl, 'qcje': qcje, 'zbqy': zbqy}}
        except Exception as e:
            res = {'res': 0, 'msg': '添加失败:' + repr(e), 'data': None}
    else:
        res = {'res': 0, 'msg': '请求错误!', 'data': None}

    return HttpResponse(json.dumps(res,default=str))

'''
删除科目  ok 
...如果删除的科目有子科目,且有数据,不能删除该付款吗
path('delekm/', Kmviews.deleKm, name='delekm'),  # get
params: id=xxxx
'''
def deleKm(request):
    if request.method=='GET':
        id=int(request.GET.get('id', '-1'))
        # 查询是否存在子科目,如果存在并有金额,则不能删除!
        childs=models.Kmb.objects.filter(_parentId=id).all()
        if childs:
            res = {'res': 0, 'msg': '删除失败:存在子科目,请清理子科目后删除!', 'data': None}
        else:
            try:
                models.Kmb.objects.filter(id=int(request.GET.get('id','-1'))).delete()
                res={'res':1,'msg':'删除成功','data':None}
            except Exception as e:
                models.Kmb.objects.filter(id=int(request.GET.get('id', '-1'))).delete()
                res = {'res': 0, 'msg': '删除失败:'+repr(e), 'data': None}
    else:
        res = {'res': 0, 'msg': '请求错误!', 'data': None}
    return HttpResponse(json.dumps(res,default=str))


'''
查询科目
path('getkm/', Kmviews.getKm, name='getkm'),  # GET
/jxc/getkm/?nodeid=1  
'''
def getKm(request):
    if request.method=='GET':
        nodeid=request.GET.get('nodeid',None) # 根节点 下的所有分支 nodeid=2 当前id为2下的所有分支
        data = models.Kmb.objects.all().order_by('_parentId', 'kmbm')  # 所有节点
        tree = genTree(nodeid, data)
        res={'res':1,'msg':'树生成成功','data':tree}
    else:
        res = {'res': 1, 'msg': '树生成成功', 'data': []}
    return HttpResponse(json.dumps(res, default=str))


'''
根据数据表生成树 JSON
1.数据表中 基本字段 id 当前节点id; _parentId 父节点ID
2.调用本函数,需要传参: nodeid--需要生成树的当前节点 ,data--数据表所有数据
    从data中 递归搜索 节点,添加的 列表 tree[] 中.
3.递归:判断 当前节点 是否为父节点
ex:
 data = models.Kmb.objects.all().order_by('_parentId', 'id') #所有节点
 nodeid=None  #根节点 下的所有分支 nodeid=2 当前id为2下的所有分支
 tree=genTree(nodeid,data)

'''
def genTree(nodeid, data):
    tree = []
    items = data.filter(_parentId=nodeid).all()
    for r in items:
        childrows = data.filter(_parentId=r.id).all()
        if childrows:
            t = genTree(r.id, data)
            msdata={
                'id': r.id, '_parentId': r._parentId,
                'kmbm': r.kmbm,'kmmc':r.kmmc,'kmxz':r.kmxz,'zbqy':r.zbqy,
                'label': r.kmbm+' '+r.kmmc, 'children': t,
                'qcsl':'0.00', 'qcje': '0.00','zbqy':r.zbqy
            }
            tree.append(msdata)
        else:
            msdata={
                'id': r.id, '_parentId': r._parentId,
                'kmbm': r.kmbm, 'kmmc': r.kmmc, 'kmxz': r.kmxz,'zbqy':r.zbqy,
                'label': r.kmbm + ' ' + r.kmmc,
                'qcsl':r.qcsl,'qcje':r.qcje,'zbqy':r.zbqy
            }
            tree.append(msdata)
    return tree

def getchild(nodeid):
    res={'leaf':0,'sumje':0}
    if not nodeid:
        return res
    rows=models.Kmb.objects.filter(_parentId=nodeid).all()
    for r  in rows:
        res['leaf']+=1
        res['sumje']+=r.qcje
        childr=models.Kmb.objects.filter(_parentId=r.id)
