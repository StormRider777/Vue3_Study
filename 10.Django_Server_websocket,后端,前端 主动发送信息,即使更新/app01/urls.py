from django.urls import path
from . import views

app_name='app01'

urlpatterns=[
    path('getdata/', views.getdata,name='getdata'),
    path('postdata/',views.postdata,name='postdata'),
    path('gettoken/',views.gettoken,name='gettoken')
]