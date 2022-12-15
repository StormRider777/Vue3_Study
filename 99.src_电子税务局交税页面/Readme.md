#Vue3中组件动画 进入离开
- template中的html
```html
<router-view v-slot="{ Component }">
    <transition name="aniview">
        <component :is="Component" />
    </transition>
</router-view>
```
- CSS 设置
```css
.aniview-enter-from,.aniview-leave-to{
    position: absolute;
    left: 220px;
    top: 70px;
    transform: translateX(100%);
    opacity: 0;
}
.aniview-enter-to,.aniview-leave-from{
    transform: translateX(0px);
    opacity: 1;
}
.aniview-enter-active,.aniview-leave-active{
    transition: all 1s
}
```
# django 后端数据服务
```python
def getyzdata(request):
    if request.method=='GET':
        querykw=request.GET.get('querykw','').strip()
        if not querykw:
            res=list(models.Yz.objects.all().values('id','name','tele','cardid','gzdw'))
        else:
            res = list(models.Yz.objects.filter(
                    Q(name__icontains=querykw) |
                    Q(gzdw__icontains=querykw) |
                    Q(cardid__icontains=querykw)
                    ).values('id', 'name', 'tele', 'cardid', 'gzdw'))

        return HttpResponse(json.dumps(res))
    else:
        data=request.POST
        if data.get('type','')=='':
            try:
                name=data['name']
                tele = data['tele']
                cardid = data['cardid']
                gzdw = data['gzdw']
                models.Yz.objects.filter(id=data['id']).update(name=name,tele=tele,cardid=cardid,gzdw=gzdw)
                res = {'res': 1, 'msg': name+'  '+tele+'修改成功!','data':data}
            except Exception as e:
                res = {'res': 0, 'msg': '更新失败:'+repr(e)}

            return HttpResponse(json.dumps(res))
        elif data.get('type','')=='add':
            name = data['name']
            tele = data['tele']
            cardid = data['cardid']
            gzdw = data['gzdw']
            try:
                models.Yz.objects.create(name=name,tele=tele,cardid=cardid,gzdw=gzdw)
                res = {'res': 1, 'msg': '增加业务记录成功', 'data': data}
            except Exception as e:
                res = {'res': 0, 'msg': '增加业务记录失败', 'data': data}

            return HttpResponse(json.dumps(res))
        elif data.get('type','')=='dele':
            id=data.get('id','')
            try:
                models.Yz.objects.filter(id=int(id)).delete()
                res = {'res': 1, 'msg': '删除成功!', 'data': data}
            except Exception as e:
                res = {'res': 0, 'msg': '删除失败!'+repr(e), 'data': data}
            return HttpResponse(json.dumps(res))
            
```

- vue vue.config.js 设置跨域访问
```javascript

module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave:false,
    devServer: {
        //open: true,
        host: 'localhost',
        port: 8080,
        //这里的ip和端口是前端项目的;下面为需要跨域访问后端项目
        proxy: {
            '/dataserver': {
                target: 'http://127.0.0.1:80',//这里填入你要请求的接口的前缀
                ws:true, //代理websocked
                changeOrigin:true,//虚拟的站点需要更管origin
                //secure: true,     //是否https接口
                pathRewrite:{
                  '^/dataserver':''//重写路径
                },
                headers: {
                    referer: 'http://localhost:8080/', //这里后端做了拒绝策略限制，请求头必须携带referer，否则无法访问后台
                }
            }
        }
    }
})


```

# Element-plus 表格的应用
- template table表格组件 paginition 分页组件
```html
<el-table :data="tableData.data.slice((Page.currentPage-1)*Page.pagesize,(Page.currentPage-1)*Page.pagesize+Page.pagesize)"
      border highlight-current-row
      :row-style="{height:'35px'}"
      :header-cell-style="{height:'35px',background:'darkgray','text-align':'center',color:'snow'}"
      :cell-style="rowcolor"
      height="540" style="width: 100%"
      @row-dblclick="handleEditrow">
    <el-table-column prop="id" label="ID" width="60"/>
    <el-table-column prop="name" label="姓名" width="100"  :show-overflow-tooltip="true"  />
    <el-table-column prop="cardid" label="证件号码" width="180"  :show-overflow-tooltip="true" />
    <el-table-column prop="tele" label="电话" width="130"  :show-overflow-tooltip="true"  />
    <el-table-column prop="gzdw" label="工作单位" :show-overflow-tooltip="true" />
    <el-table-column label="操作">
        <template #default="scope">
            <el-button type='primary' @click="handleEdit(scope.$index, scope.row,scope)" style="width: 60px;height: 25px">
                <el-icon> <Edit/></el-icon>修改
            </el-button>
            <el-button type="danger" @click="handleDelete(scope.$index, scope.row)" style="width: 60px;height: 25px">
                <el-icon><Delete /></el-icon>删除
            </el-button>
        </template>
    </el-table-column>
</el-table>

<el-pagination
  v-model:current-page="Page.currentPage"
  v-model:page-size="Page.pagesize"
  :page-sizes="[10,20,50,100]"
  :small="Page.small"
  :disabled="Page.disabled"
  :background="Page.background"
  layout="sizes, prev, pager, next, jumper,->,total "
  :total="Page.total"
  @size-change="handleSizeChange"
  @current-change="handleCurrentChange"
  :hide-on-single-page="false"
  prev-text="上一页"
  next-text="下一页"
  total-text="总记录数:"
  style="margin: 10px auto"
/>

```
- 为表格table 获取数据 setup(){}
```javascript
onMounted(()=>{
    axios({
        url:"/dataserver/data/getyzdata/",
        method:'get',
        params:{}
    }).then((res)=>{
        let s=res.data
        s.forEach((r)=>{
            Page.total++
            tableData.data.push(r)
        })

    }).catch((err)=>{
        tableData.data.push({name:'发生错误',cardid:err.code,tele:err.name,gzdw:err.message})
    })
})
```
- 查询数据
```javascript
const querydata=()=>{
    tableData.data.splice(0,tableData.data.length) //情况表格数据
    Page.total=0 //分页组件清零

    axios({
        url:`/dataserver/data/getyzdata/?querykw=${tableData.querykw}`,
        method:'get',
        params:{}
    }).then((res)=>{
        let s=res.data
        s.forEach((r)=>{
            Page.total++
            tableData.data.push(r)
        })
    }).catch((err)=>{
        tableData.data.push({name:'发生错误',cardid:err.code,tele:err.name,gzdw:err.message})
    })
}

```    
- 修改数据
```javascript
const updaterow=()=>{
    dialogupdatedata.value=false //关闭dialog
    let data={
        id:updateform.id,
        name:updateform.name,
        tele:updateform.tele,
        gzdw:updateform.gzdw,
        cardid:updateform.cardid
    }
    axios({
        url:`/dataserver/data/getyzdata/`,
        method:'post',
        data,
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    }).then(res=>{
        let data=res.data.data

        for (let i=0;i<=tableData.data.length;i++){
            let r=tableData.data[i]
            if (r.id===parseInt(data.id)){
                r.name=data.name
                r.tele=data.tele
                r.cardid=data.cardid
                r.gzdw=data.gzdw
                break
            }
        }
        ElMessageBox.alert(res.data.msg,'提示',{type:'success'})
    }).catch(err=>{
        console.log(err.message)
    })
}

```
- 增加数据
```javascript
const submitbtn=()=>{
    axios({
        url:`/dataserver/data/getyzdata/`,
        method:'post',
        data:{type:'add',
                name:data.name,
                cardid:data.cardid,
                tele:data.tele,
                gzdw:data.tele,
                hobby:data.hobby.join(','),
                sex:data.sex
        },
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
    }).then(res=>{
        console.log(res.data)
        ElMessageBox.alert(res.data.msg+' <strong style="color:red">'+res.data.data.name+"</strong>",'提示',{
            type:'success',
            dangerouslyUseHTMLString:true
        }).then(r=>{
            data.gzdw=''
            data.name=''
            data.tele=''
            data.cardid=''
            data.hobby=[]
            data.sex=''
        })
    })
}

```
- 删除数据
```javascript
const handleDelete=(index,row)=>{
    ElMessageBox.confirm(
            `确认删记录:<strong style="margin-left:10px;color:red"> ${row.name} ${row.cardid}</strong>`,
            '请确定是否删除',
            {
                dangerouslyUseHTMLString:true,
                confirmButtonText:'删除',
                cancelButtonText:'取消',
                closeOnPressEscape:true,
                closeOnClickModal:false,
                type:'warning'
            }
        ).then(res=>{
            axios({
                url:`/dataserver/data/getyzdata/`,
                method:'post',
                data:{type:'dele',id:row.id},
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
            }).then(res=>{
                let r=(Page.currentPage-1)*Page.pagesize+index
                tableData.data.splice(r,1)
                ElMessageBox.alert(
                    `删除了:<strong style="color: red"> ${ row.name } ${ row.cardid } </strong>`,'提示',
                    {
                        dangerouslyUseHTMLString:true,
                        confirmButtonText:'确定',
                        closeOnClickModal:false,
                        type:'warning'
                    })
            }).catch(err=>{
                console.log('失败了:',err.message)
            })
        }
    )
}

```
#关于Nprogress的用法
- 安装
```text
npm install --save nprogress
```
-在路由js中引入
```javascript
import NProgress from "nprogress"; // 导入 nprogress模块

import "nprogress/nprogress.css"; // 导入样式，否则看不到效果

NProgress.configure({ showSpinner: false }); // 显示右上角螺旋加载提示

```
-前置路由守护
```javascript
router.beforeEach((to, from, next) => {

    NProgress.start(); //开启进度条
    
    //中间写其他的项目中所需要的一些代码，例如有些网页只有登录了才能进，在这里可以做出判断，判断完了满足要求后就可以放行 next()
    
    next();

});
```
-后置路由守护
```javascript
router.afterEach(() => {

    NProgress.done(); //完成进度条

});
```
-设置Nprogress的其他显示样式
```css
#nprogress .bar {

  background: blue !important;    //这里可以随便写颜色

}
```

