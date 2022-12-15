# Generated by Django 4.0.3 on 2022-12-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_user_jmpwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentmenuid', models.IntegerField(default=0, verbose_name='父菜单ID')),
                ('path', models.CharField(default='', max_length=100, verbose_name='路由路径')),
                ('pagefilename', models.CharField(default='', max_length=100, verbose_name='页面文件名称')),
                ('iconname', models.CharField(default='', max_length=100, verbose_name='菜单图标')),
                ('menutitle', models.CharField(default='', max_length=200, verbose_name='菜单名称')),
                ('isuse', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name': '功能菜单表',
                'verbose_name_plural': '功能菜单表',
            },
        ),
    ]
