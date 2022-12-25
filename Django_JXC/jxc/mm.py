#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :mm.py
# @Time      :2022/12/17 0:05
# @Author    :StormRider

import hashlib

def md5mm(s=''):
    s=s[::-1]
    return hashlib.md5(s.encode('utf-8')).hexdigest()

