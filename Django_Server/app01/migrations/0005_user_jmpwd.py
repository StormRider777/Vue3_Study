# Generated by Django 4.0.3 on 2022-12-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_rename_carid_yz_cardid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='jmpwd',
            field=models.CharField(default='', max_length=100, verbose_name='密文密码'),
        ),
    ]
