#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: Vue3_study
# @FileName  :App01Form.py
# @Time      :2022/11/20 15:42
# @Author    :StormRider
from django.forms import ModelForm,CharField,widgets as wid,ValidationError
from . import models

class UserRegForm(ModelForm):
    repwd=CharField(min_length=4,max_length=20,label='重复密码',
                    widget=wid.PasswordInput(attrs={'style': 'width:300px;height:25px;', 'placeholder': '重复密码...',}),)
    class Meta:
        model=models.User
        fields=['name','pwd','repwd','tele','photo',]
        widgets={
            'name':wid.TextInput(attrs={'style':'width:300px;height:25px;','placeholder':'请输入姓名...','autocomplete':'off'}),
            'pwd': wid.PasswordInput(attrs={'style': 'width:300px;height:25px;', 'placeholder': '请输入密码...',}),
            'tele': wid.TextInput(attrs={'style': 'width:300px;height:25px;', 'placeholder': '手机号码...','autocomplete':'off' }),
            'photo': wid.FileInput(attrs={'style': 'width:300px;height:25px;margin-bottom:10px', 'placeholder': '选择文件...',})
        }

    def clean(self):
        if self.cleaned_data.get('pwd')!=self.cleaned_data.get('repwd') and self.cleaned_data.get('pwd')!='':
            raise ValidationError('两次输入密码不一致,不密码为空!')
        else:
            return self.cleaned_data