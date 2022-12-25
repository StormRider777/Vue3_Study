#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :test2.py
# @Time      :2022/12/22 22:57
# @Author    :StormRider

import sys
sys.path.extend(['D:\\Pythonstudy\\Vue3_study\\Django_JXC\\'])
import os

os.environ['DJANGO_SETTINGS_MODULE']='Django_JXC.settings'
import django
django.setup()

# Create your tests here.

from jxc import models

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
def genTree(nodeid,data):
    tree = []
    items=data.filter(_parentId=nodeid).all()
    for r in items:
        childrows = data.filter(_parentId=r.id).all()
        if childrows:
            t=genTree(r.id,data)
            tree.append({'id': r.id, '_parentId': r._parentId, 'kmbm': r.kmbm, 'label': r.kmmc,'children':t})
        else:
            tree.append({'id': r.id, '_parentId': r._parentId, 'kmbm': r.kmbm, 'label': r.kmmc})
    return tree

if __name__ == '__main__':
    data = models.Kmb.objects.all().order_by('_parentId', 'id')
    nodeid=None
    tree=genTree(nodeid,data)
    print(tree)