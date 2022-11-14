# Win7 32位旗舰版安装node.js vue3 @vue/cli5
## 1.安装 node.js 12.22版本,13以上版本不能正常安装@vue/cli,14以上版本系统最低要求win8
## 2.下载的node.js
### 历史版本:https://nodejs.org/zh-cn/download/releases/ ,选择12.22.12,
### 这个版本能安装vue3及脚手架,
### 下载node-v12.22.12-win-x86.zip,解压,不必setup,在c: 建立 Node_JS文件夹,将解压文件放进该目录下.  
## 3.配置npm: 
### Node_JS文件夹下创建  node_cache  node_global文件
### 设置全局包目录:
### npm config set prefix “c:\Node_JS\node_global” 
### 设置缓存目录
### npm config set cache “c:\Node_JS\node_cache”  
### 设置淘宝 安装包镜像:
### npm config set registry https://registry.npm.taobao.org
### 查看配置文件:
#### Npm config ls
### 查看node 版本
#### node –v
### 查看npm 版本
####   npm –v
### 配置文件在用户文档夹内 搜索 .npmrc
## 4.安装vue3
### Npm install –g vue
### 安装 @vue/cli
### npm install –g @vue/cli
### 查看vue的版本: npm info vue
### 查看@vue/cli 版本 vue -V  或 vue –version
## 5.使用脚手架创建 vue3项目:
### 在cmd 中 切换到 F:盘,或其他盘,不要在C:盘
### Vue create vue3_study 
### 在f:盘下 生成了 vue3_study项目 ,npm run serve 看看是否正常启动.

## 6.Github: 
### https://github.com/StormRider777/Vue3_Study.git 
# vue3_study

# 关于 Django 
## 1.在vu项目中手动创建 
- 在控制台中执行  django-admin createproject 项目名
- 命令行下:cd 项目, 创建 app01应用: python manage.py startapp app01
- 设置 settings 在app01中创建 模板及 views ,
- urls 中配置 app01.
- 如果在 pycharm 中书写Django模板代码没有自动提示,pycharm settings languages & frameworks django 项
- 设置 enagble django support ,django项目的目录.以及settings位置,以及 manage.py

# Django--Vue 通信 
- 1.如果 vue 前端,与Django提供的后端服务不是同域,则需要在 vue.config.js设置
```Vue  vue.config.js
module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave:false,

	devServer:{
	    //host: 'localhost', //target host
	    //port: 8080,
	    //proxy:{'/django':{}},代理器中设置/api,项目中请求路径为/api的替换为target
	    proxy:{
	        '/django':{
	            target: 'http://127.0.0.1:80/data/',//代理地址，这里设置的地址会代替axios中设置的baseURL
	            changeOrigin: true,// 如果接口跨域，需要进行这个参数配置
	            //ws: true, // proxy websockets
	            //pathRewrite方法重写url
	            pathRewrite: {
	                '^/django': ''
	                //pathRewrite: {'^/django': '/'} 重写之后url为 http://127.0.0.1:80/xxxx
	                //pathRewrite: {'^/django': '/django'} 重写之后url为 http://192.168.1.16:8085/api/xxxx
	           }
	    }}
	},
})

```
- 2.Django 的views代码:
```python

from django.shortcuts import render,HttpResponse
from django.middleware.csrf import get_token
import random
import json
# Create your views here.
def index(request):
    return render(request,'app01/index.html')

def gettoken(request):
    token=get_token(request)
    return HttpResponse(token)

def getdata(request):

    data=[
        {'id': '001', 'name': '东方不败', 'salary': random.randint(10000,99999)},
        {'id': '002', 'name': '欧阳锋', 'salary': random.randint(10000,99999)},
        {'id': '003', 'name': '黄老邪', 'salary': random.randint(10000,99999)},
        {'id': '004', 'name': '洪七公', 'salary': random.randint(10000,99999)},
        {'id': '005', 'name': '张三丰', 'salary': random.randint(10000,99999)},
        {'id': '006', 'name': '岳不群', 'salary': random.randint(10000,99999)},
        {'id': '007', 'name': '玄冥二老', 'salary': random.randint(10000,99999)},
        {'id': '008', 'name': '赵敏', 'salary': random.randint(10000,99999)},
        {'id': '009', 'name': '张无忌', 'salary': random.randint(10000,99999)},
        {'id': '010', 'name': '扫地僧', 'salary': random.randint(10000,99999)},
        {'id': '011', 'name': '韦一笑', 'salary': random.randint(10000,99999)},
        {'id': '012', 'name': '郭靖', 'salary': random.randint(10000,99999)},
    ]
    mid=request.GET.get('id', '')
    if not mid:
        res=random.choice(data)
        res = {'res': 1, 'msg': f'随机找到了一条: id={mid} 的数据', 'row': res}
    else:
        findr=False
        for r in data:
            if r['id']==mid:
                res = {'res': 1, 'msg': f'成功找到了: id={mid} 的数据', 'row': r}
                findr=True
                break
        if not findr:
            res={'res':0,'msg':f'没有找到: id={mid} 的数据','row':{}}
    return HttpResponse(json.dumps(res))

def postdata(request):
    print(request.POST)
    if request.POST:
        r={'res':1,'msg':'收到了POST数据!','data':request.POST}
    else:
        r = {'res': 0, 'msg': '没有POST数据!', 'data': request.POST}
    return HttpResponse(json.dumps(r))



```
- 3.vue 代码:
```vue

<template>
    <div>

        <div class="reqtype">
            <button @click="getdata">向 Django-server GET请求一条数据</button>
            <h4 v-text="data.token"></h4>
            <hr>
            <div id="getres" v-text="data.getres"
                 style="line-height:27px;text-align: left;padding:5px 5px 5px 5px;overflow:auto;font-size:16px;color:yellow;border-radius:10px;width:80%;margin: 10px auto;height: 100px;background:#030303">

            </div>
        </div>
        <hr>
        <div class="reqtype">
            <button @click="postdata">向 Django-server POST一条数据</button>
            <hr>
            <div id="getpost" v-text="data.postres"
                 style="line-height:27px;text-align: left;padding:5px 5px 5px 5px;overflow:auto;font-size:16px;color:red;border-radius:10px;width:80%;margin: 10px auto;height: 100px;background:#131313">

            </div>
        </div>
    </div>
</template>

<script>
    import Getdatas from '../hooks/GetDatas'
    import {reactive} from 'vue'
    export default {
        name: "MyPage",
        setup(){
            let data=reactive({})

            function getdata(){
                data.getres=Getdatas.getdata()

            }
            function postdata(){
                data.postres=Getdatas.postdata()
            }

            return {data,getdata,postdata}
        }
    }
</script>

<style scoped>
    .reqtype{
        width:60%;
        margin: 10px auto;
        background: blanchedalmond;
        border-radius:5px;
        text-align: center;
        padding-bottom: 10px;
        padding-top: 10px;
    }

    button{
        height: 38px;
        width: 300px
    }
</style>

```
- 5.GetDatas.js GET请求 和POST请求的js 
```javascript
export default {
    gettoken() {
        let xhr=new XMLHttpRequest()
        xhr.open('GET','/django/gettoken/',false)
        xhr.send()
        return xhr.responseText
    },
    getdata() {
        let xhr=new XMLHttpRequest()
        let mid=Math.ceil(Math.random()*15).toString().padStart(3,'0')
        xhr.open('GET',`/django/getdata/?id=${mid}`,false)
        xhr.send()
        return JSON.parse(xhr.responseText)
    },

    postdata() {
        let fd=new FormData()
        fd.append('id',Math.ceil(Math.random()*1000).toString().padStart(3,'0'))
        fd.append('name','Vue测试POST数据')
        fd.append('salary',Math.ceil(Math.random()*100000))
        let xhr=new XMLHttpRequest()
        xhr.open('POST','/django/postdata/',false)
        xhr.setRequestHeader('X-CSRFToken',this.gettoken())
        xhr.send(fd)
        return JSON.parse(xhr.responseText)
    }
}


```





