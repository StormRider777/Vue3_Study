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
ASGI_APPLICATION='Django_Server.asgi.application'

```
- 修改 asgi.py
```python




```

