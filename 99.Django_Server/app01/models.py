from django.db import models

# Create your models here.


class Yz(models.Model):
    name=models.CharField(max_length=50,default='',db_index=True,blank=False,null=False)
    cardid=models.CharField(max_length=20,default='',verbose_name='证件号码')
    gzdw=models.CharField(max_length=100,default='',verbose_name='工作单位')
    tele=models.CharField(max_length=20,default='',verbose_name='电话')
    class Meta:
        verbose_name='业主信息表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return f"{self.name} {self.tele} {self.cardid} {self.gzdw}"

class Lf(models.Model):
    lh = models.CharField(max_length=20, default='', unique=True, null=False, blank=False, verbose_name='楼号')
    fh = models.CharField(max_length=20, default='', unique=True, null=False, blank=False, verbose_name='房号')
    jzmj = models.DecimalField(max_digits=15,decimal_places=2, default=0.00, verbose_name='建筑面积')
    yz = models.ForeignKey(to=Yz, on_delete=models.DO_NOTHING, verbose_name='业主')

    class Meta:
        verbose_name = '楼房'
        verbose_name_plural=verbose_name
    def __str__(self):
        return f"{self.lh}-{self.fh}"

class WyfBill(models.Model):
    sj=models.DateTimeField(default='',verbose_name='日期')
    lj=models.ForeignKey(to=Lf,on_delete=models.DO_NOTHING,verbose_name='房屋')
    billno=models.CharField(max_length=20,default='',verbose_name='账单编号')
    zy=models.CharField(max_length=80,default='',verbose_name='摘要')
    yingjiaomoney=models.DecimalField(max_digits=15,decimal_places=2,default=0,verbose_name='应交数额')
    yijiaomoney=models.DecimalField(max_digits=15,decimal_places=2,default=0,verbose_name='已交数额')
    class Meta:
        verbose_name='物业费账单表'
        verbose_name_plural=verbose_name
    def __str(self):
        return  f"{self.sj} {self.zy} {self.billno} {self.yingjiaomoney} {self.yijiaomoney}"


class User(models.Model):
    name=models.CharField(max_length=100,default='',verbose_name='操作员')
    pwd=models.CharField(max_length=100,default='',verbose_name='登录密码')
    jmpwd=models.CharField(max_length=100,default='',verbose_name='密文密码')
    photo=models.ImageField(upload_to='app01/',verbose_name='头像')
    tele=models.CharField(max_length=20,default='',verbose_name='手机')
    createtime=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        verbose_name='操作用户表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return f"{self.name} {self.pwd} {self.tele} {self.photo} "+self.createtime.strftime('%Y-%m-%d %H:%M:%S')

class Menus(models.Model):
    parentmenuid=models.IntegerField(default=0,verbose_name='父菜单ID')
    path=models.CharField(max_length=100,default="",verbose_name='路由路径')
    pagefilename=models.CharField(max_length=100,default="",verbose_name='页面文件名称')
    iconname=models.CharField(max_length=100,default="",verbose_name='菜单图标')
    menutitle=models.CharField(max_length=200,default="",verbose_name='菜单名称')
    isuse=models.BooleanField(default=True,verbose_name='是否可用')
    
    class Meta:
        verbose_name='功能菜单表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return f"{self.parentmenuid} {self.path} {self.menutitle}"
