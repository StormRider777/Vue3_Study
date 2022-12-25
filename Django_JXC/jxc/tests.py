from django.test import TestCase
import sys
sys.path.extend(['D:\\Pythonstudy\\Vue3_study\\Django_JXC\\'])
import os

print(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE']='Django_JXC.settings'
import django
django.setup()

# Create your tests here.
from jxc import models

# 清空所有账簿数据表

models.Kmb.objects.all().delete()
models.Kmye.objects.all().delete()
models.Mxz.objects.all().delete()
print('0')
#增加科目

models.Kmb.objects.create(id=1,_parentId=None,kmbm='1001',kmmc='现金',kmxz=1)
models.Kmb.objects.create(id=2,_parentId=None,kmbm='1002',kmmc='笑傲江湖',kmxz=1)
models.Kmb.objects.create(id=3,_parentId=None,kmbm='1023',kmmc='存货',kmxz=1)
models.Kmb.objects.create(id=4,_parentId=None,kmbm='1004',kmmc='其他应收款',kmxz=1)

models.Kmb.objects.create(id=5,_parentId=None,kmbm='2001',kmmc='借款',kmxz=1)
models.Kmb.objects.create(id=6,_parentId=None,kmbm='2002',kmmc='应付账款',kmxz=1)
models.Kmb.objects.create(id=7,_parentId=None,kmbm='2023',kmmc='其他应付款',kmxz=1)

models.Kmb.objects.create(_parentId=1,kmbm='100101',kmmc='人民币',kmxz=1)

row1=models.Kmb.objects.create(_parentId=2,kmbm='100201',kmmc='东方不败',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020101',kmmc='东方不败_侍从1',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020102',kmmc='东方不败_侍从2',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020103',kmmc='东方不败_侍从3',kmxz=1)

row2=models.Kmb.objects.create(_parentId=3,kmbm='102301',kmmc='钢材',kmxz=1)
models.Kmb.objects.create(_parentId=3,kmbm='102302',kmmc='木材',kmxz=1)
models.Kmb.objects.create(_parentId=row2.id,kmbm='10230101',kmmc='螺纹钢',kmxz=1)
models.Kmb.objects.create(_parentId=row2.id,kmbm='10230102',kmmc='盘条',kmxz=1)
models.Kmb.objects.create(_parentId=row2.id,kmbm='10230103',kmmc='方管',kmxz=1)
models.Kmb.objects.create(_parentId=row2.id,kmbm='10230104',kmmc='角钢',kmxz=1)

models.Kmb.objects.create(_parentId=row1.id,kmbm='10020104',kmmc='东方不败_侍从4',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020105',kmmc='东方不败_侍从5',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020106',kmmc='东方不败_侍从6',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020107',kmmc='东方不败_侍从7',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020108',kmmc='东方不败_侍从8',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020109',kmmc='东方不败_侍从9',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020110',kmmc='东方不败_侍从10',kmxz=1)
models.Kmb.objects.create(_parentId=row1.id,kmbm='10020111',kmmc='东方不败_侍从11',kmxz=1)








print('1')
#增加科目余额
models.Kmye.objects.create(kmb_id=1,qcje=1000,jfje=10501.52,dfje=1045.85)
models.Kmye.objects.create(kmb_id=2,qcje=33000,jfje=1050.90,dfje=10300.52)
models.Kmye.objects.create(kmb_id=3,qcje=400,jfje=1500.70,dfje=52.05)
models.Kmye.objects.create(kmb_id=4,qcje=600,jfje=10500.62,dfje=520.45)
models.Kmye.objects.create(kmb_id=5,qcje=7000,jfje=12500.75,dfje=562.25)
models.Kmye.objects.create(kmb_id=6,qcje=8000,jfje=15890.85,dfje=8549.29)
models.Kmye.objects.create(kmb_id=7,qcje=1900,jfje=1566.52,dfje=1580.70)

print('2')
#增加明细账业务
models.Mxz.objects.create(ywxh=1,kmb_id=1,jfje=16025.28)
models.Mxz.objects.create(ywxh=1,kmb_id=2,dfje=16025.72)
models.Mxz.objects.create(ywxh=2,kmb_id=1,jfje=1025.26)
models.Mxz.objects.create(ywxh=2,kmb_id=3,dfje=1625.21)
models.Mxz.objects.create(ywxh=3,kmb_id=4,jfje=16025.72)
models.Mxz.objects.create(ywxh=3,kmb_id=2,jfje=163005.62)
models.Mxz.objects.create(ywxh=3,kmb_id=3,dfje=164455.02)
models.Mxz.objects.create(ywxh=3,kmb_id=1,dfje=12105.27)
models.Mxz.objects.create(ywxh=4,kmb_id=1,dfje=60325.26)
models.Mxz.objects.create(ywxh=4,kmb_id=3,jfje=6525.42)
models.Mxz.objects.create(ywxh=5,kmb_id=4,dfje=6055.32)
models.Mxz.objects.create(ywxh=5,kmb_id=6,jfje=26025.12)

print('3')

# row=models.Kmye.objects.raw('select id,qcje,jfje,dfje,qcje+jfje-dfje as qmje1 from jxc_kmye')
# row[3].qmje1
# row[2].qmje1
# row.columns
# for r in row:
#     print(r.qmje1)
# from django.db.models import Max,Min,Sum,Count,Avg
# res = models.Kmye.objects.aggregate(Max('jfje'), Min('jfje'), Sum('jfje'), Count('jfje'), Avg('jfje'))

# models.Mxz.objects.filter(kmb__kmbm='1002').aggregate(Sum('jfje'),Sum('dfje'))
#out: {'jfje__sum': Decimal('17050.5400000000'), 'dfje__sum': Decimal('72430.5300000000')}