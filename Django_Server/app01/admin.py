from django.contrib import admin
from . import models
# Register your models here.
from django.utils.safestring import mark_safe

@admin.register(models.User)
class User(admin.ModelAdmin):
    #models=models.User
    hange_form_template = 'admin/extras/record_change_form.html'

    list_display = ['createtime','img','name','pwd','tele',]
    search_fields = ['name','tele']
    list_filter = ['name','tele']
    list_per_page = 5

    list_display_links = ['name',]
    list_editable = ['tele',]


    @admin.display(description='头像')
    def img(self,obj):
        #print('img:', self, obj)
        div=f"<img src='/media/{obj.photo}' style='height:50px;'>"
        return mark_safe(div)

    actions = ['btn1', 'btn2']
    def btn1(self,request,queryset):
        pass
        #print('btn1:',self,request,queryset)

    btn1.short_description='打印'
    btn1.icon='fa fa-print '
    btn1.type='success'
    btn1.style="font-size:25px"

    def btn2(self,request,queryset):
        pass
        #print('btn2')

    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
