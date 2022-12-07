#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :myfunc.py
# @Time      :2022/11/28 13:27
# @Author    :StormRider


import random
import os
import sys
from pathlib import Path
sys.path.append(r"d:\pythonstudy\vue3_study\django_server")
BASE_DIR = Path(__file__).resolve().parent.parent

# print(BASE_DIR,os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"Django_Server.settings")
import django
django.setup()

from app01.models import Yz

def randname():  #随机姓名
    '''
    import randname
    用法: name=randname()
    :return:
    '''
    firstname = '李、王、张、刘、陈、杨、黄、赵、周、吴、徐、孙、朱、马、胡、郭、林、何、' \
                '高、梁、郑、罗、宋、谢、唐、韩、曹、许、邓、萧、冯、曾、程、蔡、彭、潘、袁、於、董、余、苏、叶、' \
                '吕、魏、蒋、田、杜、丁、沈、姜、范、江、傅、钟、卢、汪、戴、崔、任、陆、廖、姚、方、金、邱、夏、谭、' \
                '韦、贾、邹、石、熊、孟、秦、阎、薛、侯、雷、白、龙、段、郝、孔、邵、史、毛、常、万、顾、赖、武、康、贺、' \
                '严、尹、钱、施、牛、洪、龚、欧阳、夏侯、慕容、东方、东郭、百里、司徒、西门、呼延、诸葛、司马、公孙'
    Blastname = '豪、言、玉、意、泽、彦、轩、景、正、程、诚、宇、澄、安、青、泽、轩、旭、恒、思、宇、嘉、宏、皓、成、宇、轩、' \
                '玮、桦、宇、达、韵、磊、泽、博、昌、信、彤、逸、柏、新、劲、鸿、文、恩、远、翰、圣、哲、家、林、景、行、律、本、' \
                '乐、康、昊、宇、麦、冬、景、武、茂、才、军、林、茂、飞、昊、明、明、天、伦、峰、志、辰、亦'
    Glastname = '佳、彤、自、怡、颖、宸、雅、微、羽、馨、思、纾、欣、元、凡、晴、玥、宁、佳、蕾、桑、妍、萱、宛、欣、灵、烟、' \
                '文、柏、艺、以、如、雪、璐、言、婷、青、安、昕、淑、雅、颖、云、艺、忻、梓、江、丽、梦、雪、沁、思、羽、羽、雅、' \
                '访、烟、萱、忆、慧、娅、茹、嘉、幻、辰、妍、雨、蕊、欣、芸、亦、涛、国、伟、华、燕、娜、丽、平、勇、永、咏、梅、妹、玫'
    first=random.choice(firstname.split("、"))
    second = random.choice(Blastname.split("、"))
    three = random.choice(Glastname.split("、"))
    return first+second+three

def randarea():
    firstname = '中国,北京,上海,广州,深圳,山东,河北,河南,广东,广西,江苏,福建,湖南,湖北,安徽,山西,贵州,黑龙江,吉林,辽宁,济南,泰安,肥城,邯郸,石家庄,南京,菏泽,江阴,连云港'
    return random.choice(firstname.split(","))

def adddata(n=2000):
    total=Yz.objects.all().count()
    for r in range(total,n):
        name = randname()
        cardid= "%02d%02d%02d%4d%02d%02d%04d"%(random.randint(10,45),random.randint(0,50),random.randint(0,50),
                                               random.randint(1920,2020),random.randint(1,13),random.randint(1,31),random.randint(0,5000))
        tele="%d%04d%04d"%(random.randint(130,190),random.randint(2000,8000),random.randint(0,10000))
        gzdw="%s_随机生成_%010d公司"%(randarea(),random.randint(100000,10000000))
        Yz.objects.create(name=name,gzdw=gzdw,tele=tele,cardid=cardid)
        print('随机记录:',name,cardid)

if __name__ == '__main__':
    adddata()