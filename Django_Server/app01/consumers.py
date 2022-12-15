'''
wsbsocket 下的 类同 views
响应 路由
'''
import asyncio
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class WsData(AsyncWebsocketConsumer):
    def __init__(self):
        self.groupname='main'
        self.tip = ''


    async def websocket_connect(self, message):  # self 当前 ws 与前端连接通道

        self.tip = '<span style="color:darkblue;width:100%;font-size:12px">' + self.channel_name + ':</span><br>'

        # 响应客户端连接请求
        # accept 允许客户端连接
        #print('收到一个连接请求..',message)
        # message :{'type': 'websocket.connect','text':'xxxxx'}
        #print('self:',self.__dict__)
        #groupname=self.scope['url_route']['kwargs']['group_name']
        #self.groupname='main'
        #print(str(self.scope['query_string'],encoding='utf8'))
        #print(self.__dict__)
        await self.channel_layer.group_add(self.groupname,self.channel_name)
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
        # await async_to_sync(self.channel_layer.group_discard)(
        #     self.groupname,
        #     self.channel_name
        # )
        await self.channel_layer.group_discard(self.groupname,self.channel_name) #self.connname)
        # raise StopConsumer()

    async def websocket_receive(self, message):
        # 浏览器基于websocket 向后端发送数据 ,自动触发接收
        #print('接受到前端的消息:',message)
        await self.channel_layer.group_send(self.groupname,{'type':'send_msg','message':message})

    async def send_msg(self,event):
        #print('name:',self.channel_name)
        msg=event['message']['text']
        if msg=='close':
            await self.send('[后端服务器关闭连接]')
            await self.close()
            return
        await self.send(self.tip+msg)


