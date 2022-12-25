# channels websocket 应用
- pip install channels
-- 此处有坑:
```text
pip install channels 默认是当前最新的版本

而:

django2.x 需要匹配安装 channels 2
django3.x 需要匹配安装 channels 3
版本搞错,django 就不能正常启动  ASGI_APPLICATION ..
经过一上午的摸排,终于,顺利启动了channels 

Django==3.2.3 # 2.1.14升级上来的，最后没影响
Channels==3.0.3
channels-redis==3.2.0

```

- 设置 settings
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'app01',
]
ASGI_APPLICATION=99.Django_Server

```
- 修改 asgi.py  ===相当于 wsgi .django启动默认 wsgi
```python

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from . import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 99.Django_Server)

# application = get_asgi_application()
application=ProtocolTypeRouter({
    'http':get_asgi_application(), #django 自动寻找 :url --views
    'websocket':URLRouter(routing.websocket_urlpatterns) router
})



```
- 设置routing.py   ====>相当于urls
```python
from django.urls import path,re_path
from app01 import consumers

websocket_urlpatterns=[
    #re_path("^wsmsg/(?P<group>\w+)",consumers.WsData.as_asgi()),
    path('wsmsg/',consumers.WsData.as_asgi())
]


```
- app下建立consumers.py ====>相当于views
```python
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
# from asgiref.sync import async_to_sync

class WsData(AsyncWebsocketConsumer):
    def __init__(self):
        self.groupname='main'

    async def websocket_connect(self, message):  # self 当前 ws 与前端连接通道
        self.connname = self.channel_name
        self.tip = '<span style="color:grey;width:100%;font-size:12px">' + self.connname + ':</span><br>'

        # 响应客户端连接请求
        # accept 允许客户端连接
        #print('收到一个连接请求..',message)
        # message :{'type': 'websocket.connect','text':'xxxxx'}
        #print('self:',self.__dict__)
        #groupname=self.scope['url_route']['kwargs']['group_name']
        #self.groupname='main'
        #print(str(self.scope['query_string'],encoding='utf8'))
        print(self.__dict__)
        await self.channel_layer.group_add(self.groupname,self.connname)
        await self.accept()
        # 如果允许连接
        #raise StopConsumer()
        await self.send(self.tip+'[已连接!]')

    async def websocket_disconnect(self, message):
        '''
         客户端主动与服务端断开连接,触发的 函数
        :param message:
        :return:
        '''
        # 服务端主动断开连接
        # self.close()

        # task_id=self.scope['utl_route']['kwwargs'].get('group')
        # async_to_sync(self.channel_layer.group_discard)(task_id,self.channel_name)
        #await self.send('断开连接')
        await self.channel_layer.group_discard(self.groupname,self.connname)
        # raise StopConsumer()

    async def websocket_receive(self, message):
        # 浏览器基于websocket 向后端发送数据 ,自动触发接收
        #print('接受到前端的消息:',message)
        await self.channel_layer.group_send(self.groupname,{'type':'send_msg','message':message})

    async def send_msg(self,event):
        #print(event)
        msg=event['message']['text']
        if msg=='close':
            await self.send('[后端服务器关闭连接]')
            await self.close()
            return
        await self.send(self.tip+msg)

```