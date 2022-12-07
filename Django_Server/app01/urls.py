from django.urls import path
from . import views

app_name='app01'

urlpatterns=[
    path('getdata/', views.getdata,name='getdata'),
    path('getyzdata/',views.getyzdata,name='getyzdata'),
    path('postdata/',views.postdata,name='postdata'),
    path('gettoken/',views.gettoken,name='gettoken'),
    path('reguser/',views.reguser,name='reguser'),
    path('listuser/',views.listusers,name='listuser'),
    path('login/',views.login,name='login'),
]