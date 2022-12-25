'''
类似于 urls.py 配置 websocket的路由
'''

from django.urls import path,re_path
from app01 import consumers

websocket_urlpatterns=[
    #re_path("^wsmsg/(?P<group>\w+)",consumers.WsData.as_asgi()),
    path('wsmsg/',consumers.WsData.as_asgi())
]

