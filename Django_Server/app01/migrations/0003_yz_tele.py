# Generated by Django 4.0.3 on 2022-11-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_user_createtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='yz',
            name='tele',
            field=models.CharField(default='', max_length=20, verbose_name='电话'),
        ),
    ]