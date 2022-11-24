"""
ASGI 支持异步 WSGI+异步 支持websocket
WSGI 本质上 支持同步第三方的 http django默认启动 用的WSGI

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from . import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Server.settings')

# application = get_asgi_application()
application=ProtocolTypeRouter({
    'http':get_asgi_application(), #django 自动寻找 :url --views
    'websocket':URLRouter(routing.websocket_urlpatterns) # router--consumers
})