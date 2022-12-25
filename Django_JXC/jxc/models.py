from django.db import models
import time
# Create your models here.
from django.utils.timezone import now
class Users(models.Model):
    name=models.CharField(max_length=100,default='',verbose_name='用户名',unique=True,db_index=True)
    account=models.CharField(max_length=20,default='',verbose_name='账号',unique=True,db_index=True)
    tele=models.CharField(max_length=11,default='',verbose_name='手机号')
    pwd=models.CharField(max_length=100,default='',verbose_name='密码')
    photo=models.CharField(max_length=100,default='',verbose_name='头像')
    createtime=models.DateTimeField(auto_now_add=True,verbose_name='注册日期')

    class Meta:
        verbose_name='用户表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return  f'{self.id} {self.account} {self.pwd} {self.name} {self.tele}'


class Kmb(models.Model):
    kmxz_choice=((1,'借方'),(2,'贷方'))
    _parentId=models.IntegerField(default=None,verbose_name='父级编码',null=True)
    kmbm=models.CharField(max_length=12,default='',verbose_name='科目编码',unique=True,db_index=True,null=False)
    kmmc=models.CharField(max_length=80,default='',verbose_name='科目名称',db_index=True,null=False)
    kmxz=models.IntegerField(choices=kmxz_choice,default=1,null=False)
    zbqy=models.BooleanField(default=False,verbose_name='账簿启用')
    qcsl=models.DecimalField(max_digits=15,default=0,decimal_places=3,verbose_name='期初数量')
    qcje = models.DecimalField(max_digits=15, default=0,decimal_places=2, verbose_name='期初金额')


    class Meta:
        verbose_name='科目表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return f'{self.id},{self._parentId},{self.kmbm} {self.kmmc} {self.get_kmxz_display()} {self.qcsl} {self.qcje}'

class Zzb(models.Model):
    rq=models.CharField(max_length=7,default='',null=False,verbose_name='日期')
    kmb=models.ForeignKey(to=Kmb,on_delete=models.CASCADE)
    jfsl =  models.DecimalField(max_digits=15,decimal_places=3,default=0,verbose_name='借方发生数量')
    jfje = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='借方发生金额')
    dfsl = models.DecimalField(max_digits=15,decimal_places=3,default=0,verbose_name='贷方方发生数量')
    dfje = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='贷方发生金额')
    class Meta:
        verbose_name='总账表'
        verbose_name_plural=verbose_name
    def __str(self):
        return f'{self.rq} {self.kmb.kmbm} {self.kmb.kmmc} {self.jfsl} {self.jfje} {self.dfsl} {self.dfje}'

class Mxz(models.Model):
    Ywzt=((0,'未复核'),(1,'已复核'),(2,'已记账'))
    ywxh=models.CharField(max_length=12,default='',verbose_name='业务编号',null=False)  #日期+序号(4位)
    kmb=models.ForeignKey(to=Kmb,on_delete=models.CASCADE)
    rq=models.DateField(default=now,verbose_name='业务日期')
    jfsl = models.DecimalField(max_digits=15, default=0,decimal_places=3, verbose_name='借方数量')
    jfje = models.DecimalField(max_digits=15, default=0,decimal_places=2, verbose_name='借方金额')
    dfsl = models.DecimalField(max_digits=15, default=0,decimal_places=3, verbose_name='贷方数量')
    dfje = models.DecimalField(max_digits=15, default=0,decimal_places=2, verbose_name='贷方金额')
    ywzt=models.IntegerField(choices=Ywzt,default=0,verbose_name='业务状态')
    srr = models.CharField(max_length=20,default='',verbose_name='输入')
    shr = models.CharField(max_length=20, default='', verbose_name='审核')
    jzr = models.CharField(max_length=20, default='', verbose_name='记账')

    class Meta:
        verbose_name='业务明细表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return f'{self.ywxh} {self.kmb.kmmc} {self.rq} {self.jfje} {self.dfje} {self.get_ywzt_display()} {self.srr} {self.shr}'



