# Vue3中组件动画 进入离开
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

#关于 element的upload组件的使用方法
```vue
<template>
    <h2>上传图片</h2>
    <hr>
    <el-upload
            v-model:file-list="fileList"
            action="/dataserver/app01/uploadimg/"
            list-type="picture-card"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            :on-success="refreshimgs"
    >
        <el-icon>
            <Plus/>
        </el-icon>
    </el-upload>
    <hr>
    <div v-for="(item,index) in imgfiles" :key="index" :id="'view_imgdiv_'+index.toString()"
         style="width: 150px;height: 158px;border-radius: 5px;border: 1px solid gray;margin: 10px 10px;
                display: inline-grid;justify-content: center;align-items: center;padding: 1px 1px">
        <img :src="'/dataserver/static/app01/upload/'+item" alt="" style="width: 100%;height: 120px;object-fit:contain">

        <el-button type="warning" @click="deleimg(item,index)" style="width: 140px;margin:2px auto" >
            <el-icon><Delete /></el-icon>
            删除
        </el-button>
    </div>
    <el-dialog v-model="dialogVisible" title="图片预览" width="500px">
            <img w-full :src="dialogImageUrl" alt="Preview Image"
                 style="width: 100%;height: 100%;object-fit: cover;border-radius: 5px;box-shadow: 0 0 3px 3px grey">
    </el-dialog>
</template>
```
```javascript

<script>
    import { ref,onMounted } from 'vue'
    import { Plus } from '@element-plus/icons-vue'
    import {ElMessage} from 'element-plus'
    import axios from 'axios'
    export default {
        name: "uploadimg",
        setup(){
            const fileList = ref([])
            const dialogImageUrl = ref('')
            const dialogVisible = ref(false)

            const handleRemove=(uploadFile, uploadFiles)=>{
                    console.log(uploadFile, uploadFiles)
            }

            const handlePictureCardPreview=(uploadFile)=>{
                    dialogImageUrl.value = uploadFile.url
                    dialogVisible.value = true
            }
            onMounted(()=>{
                getfiles()
            })
            const imgfiles=ref([])

            const refreshimgs=(upf,f)=>{
                console.log(upf,f)
                getfiles()
                console.log(imgfiles.value)
            }

            let getfiles=()=>{
                axios.get('/dataserver/app01/getimgs/').then(res=>{
                    imgfiles.value=res.data
                })
            }

            let deleimg=(fname,index)=>{
                // let fd=new FormData()
                // fd.append('fname',fname)
                axios({
                    method:'get',
                    url: '/dataserver/app01/deleimg/',
                    params: {fname:fname}
                }).then(res=>{
                    if (!res.data.res){
                        ElMessage({message:'发生错误:'+res.data.msg,type:'warning'})
                    }else{
                        ElMessage({message:'删除文件:'+fname+'成功!',type:'success'})
                        let divno='view_imgdiv_'+index.toString()
                        document.getElementById(divno).remove()
                    }

                }).catch(e=>{
                    ElMessage({message:'发生错误:'+e.message,type:'error'})
                    console.log(e.message)
                })
            }


            return {fileList,dialogImageUrl,dialogVisible,handlePictureCardPreview,handleRemove,imgfiles,refreshimgs,deleimg}
        }
    }
</script>

```
```python
def uploadimg(request):
    mfile=request.FILES.get('file',None)
    # print(os.getcwd())
    # print(mfile,mfile.name,mfile.size,mfile.content_type)
    if mfile:
        tfile=os.path.join('app01','static','app01','upload',mfile.name)
        with open(tfile,'wb') as f:
            for c in mfile.chunks():
                f.write(c)
        return HttpResponse('ok')
    else:
        return HttpResponse('No File Found!')

def getimglist(request):
    imgpath=os.path.join('app01','static','app01','upload')
    files=os.listdir(imgpath)
    if files:
        return HttpResponse(json.dumps(files))
    else:
        return HttpResponse(json.dumps(None))

def deleimg(request):
    mdelef=request.GET.get('fname','')
    fpath=os.path.join('app01','static','app01','upload',mdelef)
    print(mdelef)
    if os.path.isfile(fpath) and mdelef:
        try:
            os.remove(fpath)
            res={'res':1,'msg':'文件:'+mdelef+':已删除!'}
        except Exception as e:
            res = {'res': 0, 'msg': repr(e)}
    else:
        res = {'res': 0, 'msg': '文件:' + mdelef + ':不存在!'}
    return HttpResponse(json.dumps(res))



```
#手动上传文件
```javascript
<el-upload class="upload-demo"
  //ref="upload"	// this.$refs.upload.submit(); 这是提交使用
  accept="application/pdf,image/png,image/jpeg,image/jpg,"	//允许上传的格式
  action="https://xxxx.com/posts/"	//这里为连接服务器的地址
  multiple		//是否支持多选文件
  :limit="3"	//最大允许上传个数
  :file-list="fileListData"		//上传的文件列表
  :on-exceed="handleExceed"		//文件超出个数限制时的钩子
  :on-change="handleChange"		//文件状态改变时的钩子，添加文件、上传成功和上传失败时都会被调用
  :on-remove="handleRemove"		//文件列表移除文件时的钩子
  :auto-upload="false"		//是否在选取文件后立即进行上传
  //:before-upload="beforeUpload"	//上传文件之前的钩子(这里用来控制文件大小、格式等，手动上传在on-change中控制)
  //:data={id:formDta.id}		//自动上传时附带的额外参数（手动上传可以在axiso中单独写）
  >
  <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
  <el-button size="small" type="success" @click="submitUpload">点击上传</el-button>
  <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
</el-upload>
//定义数据信息
data(){
	return{
		id:'xxxx',//参数id
		fileListData:[],//上传文件列表
	}
}
//方法函数如下
methods:{
	//上传文件前进行文件格式、大小的校验
	beforeUpload(file,fileList){
		let fileTypeList = ["pdf","png","jpeg","jpg"]	//可以上传的文件后缀名
		let fileType = file.name.substring(file.name.lastIndexOf(".") + 1)//获取上传文件的后缀名
		const isType = (fileTypeList.indexOf(fileType ) === -1)//判断类型是否符合
		const isLtXM = file.size / 1024 / 1024 < 10 //上传文件小于10MB
		if(isType){
			this.$message.error('只能上传pdf，png，jpeg，jpg格式文件')
			//fileList.pop()//删除不符合的文件  这两个方法随便选择一个都行
			fileList.splice(fileList.indexOf(file),1)//删除不符合的文件
			return false；
		}else if(!isLtXM ){
			this.$message.error('文件大小不能超过10MB')
			fileList.splice(fileList.indexOf(file),1)//删除不符合的文件
			return false；
		}
	},
	//文件超出个数限制的钩子
	handleExceed(files,fileList){
		this.$message.warning(`当前限制上传3个文件，本次选择了${files.length}个文件，共选择了${files.length + fileList.length}个文件`)
	},
	//上传文件事件
	handleChange(file,fileList){
		if(file.status != 'ready'){return false;}//文件准备好后再执行 解决两次调用的问题
		this.beforeUpload(file,fileList)//进行文件校验  （自动上传配合 before-upload 使用，）手动上传需要单独校验
		fileList.forEach(item=>{//循环数组进行base64转换
			//调用base64方法进行数据的转换(方法在下面定义)
			this.getBase64(item.raw).then(res=>{
				item.url= res	//在原数组中每个数据添加属性url和转换后的base64编码值（这里我放在原字段中方便删除文件列表使用,也可以自定义数组存放根据个人喜好）
			})
		})
		//转换base64是异步方式需要一些时间  这里赋值建议延迟一下
		setTimeout(()=>{
			this.fileListData = fileList
		},1000)
	},
	//base64编码转换方法
	getBase64(file){
		return new Promise((resolve,reject)=>{
			let reader = new FileReader()	//定义方法读取文件
			reader.readAsDataURL(file)	//开始读文件  本身是图片的二进制数据 进行base64加密形成字符串
			reader.onload = ()=> resolve(reader.result)//成功返回对应的值 reader.result可以直接放在img标签中使用
			reader.onerror = ()=> reject(error)//失败返回失败信息
		})
	},
	//文件列表移除文件时钩子
	handleRemove(file，fileList){
		this.fileListData = fileList
		//或者使用下面方法
		//this.fileListData.splice(this.fileListData.indexOf(file),1)//删除不符合的文件
	},
	//提交方法
	submitUpload(){
		let base64FileList = []
		this.fileListData.forEach(file=>{
			base64FileList.push(file.url)
		})
		//第一种ref提交 数据在:data={id:formDta.id,files:base64FileList}配置
		this.$refs.upload.submit();
		//第二种：axios 自定义提交
		this.$axios('https://xxxx.com/posts/','POST',{
			id:this.id,
			files:base64FileList //这里base64FileList 为后台需要的参数[1,2]形式 根据自己需要修改
		}).then(res=>{
			console.log(res,'请求返回信息')
			this.$message.success('文件添加成功了')
		})
	},	
}
```
-  还可以使用FormData() 方法数据信息提交 
```javascript
//上传文件事件
	handleChange(file,fileList){
		if(file.status != 'ready'){return false;}
		this.beforeUpload(file,fileList)
		this.fileListData = fileList
	},
	//提交方法中进行转换
	submitUpload(){
		//创建新的数据对象
		let newFormData = new FormData()
		let fileName = []//存储文件名字
		this.fileListData.forEach(file=>{
			newFormData.append('file',file.raw)
			fileName.push(file.name)
		})
		newFormData.append('fileName',fileName)
		cosole.log(newFormData.getAll('file'))//查看文件信息
		//提交数据
		this.$axios('https://xxxx.com/posts/','POST',{
			id:this.id,
			files:newFormData
		}).then(res=>{
			console.log(res,'请求返回信息')
			this.$message.success('文件添加成功了')
		})
	} 
```
# element table 数据导出到EXCEL
```vue
<template>
    <h2>表格数据导出EXCEL</h2>
    <hr>
    <div style="width: 100%;height: 50px">
        <el-button color="red" @click="exportExcel()">
            <el-icon color="#030303" size="18px"><DocumentCopy /></el-icon>
            导出EXCEL
        </el-button>
    </div>
    <el-table :data="tableData.viewdata"
              height="500"
              :highlight-current-row="true"
              border
              id="outtable"
    >
        <el-table-column prop="id" label="ID" width="180"/>
        <el-table-column prop="name" label="姓名" width="180"/>
        <el-table-column prop="salary" label="战力"/>
    </el-table>
    <el-pagination style="margin-top: 10px"
                   v-model:current-page="page.currentPage"
                   v-model:page-size="page.pageSize"
                   :page-sizes="[3,10, 20, 30, 100]"
                   :small="false"
                   :disabled="false"
                   :background="true"
                   :pager-count="5"
                   layout="total, sizes, prev, pager, next, jumper"
                   :total="tableData.data.length"
                   @size-change="handleSizeChange"
                   @current-change="handleCurrentChange"
    />
</template>
```
```javascript
 import {onMounted,reactive} from 'vue'
    import axios from 'axios'
    //xlsx 与 file-saver依赖
    //npm install --save xlsx file-saver
    import {ElMessage} from 'element-plus'
    import FileSaver from "file-saver";
    import * as XLSX from "xlsx";

    export default {
        name: "explortExcel",
        setup(){
            const tableData=reactive({
                data:[],
                viewdata:[]
            })
            const page=reactive({
                currentPage:1,
                pageSize:10
            })
            onMounted(()=>{
                axios({
                    method:'get',
                    url:'/dataserver/app01/getalldata/'
                }).then(res=>{
                    tableData.data=res.data
                    handleCurrentChange(1)
                })
            })
            let handleCurrentChange=(number)=>{
                tableData.viewdata=tableData.data.slice((number-1)*page.pageSize,number*page.pageSize)
            }
            let handleSizeChange=(number)=>{
                tableData.viewdata=tableData.data.slice((page.currentPage-1)*page.pageSize,page.currentPage*page.pageSize)
            }

            let exportExcel = () => {
                /* generate workbook object from table */
                var xlsxParam = { raw: true }
                let el=document.querySelector('#outtable')
                if (!el){
                    ElMessage('获取表格元素出现错误')
                    return false
                }
                var wb = XLSX.utils.table_to_book(el,xlsxParam)

                /* get binary string as output */
                var wbout = XLSX.write(wb, {bookType: 'xlsx', bookSST: true, type: 'array'})
                try {
                    FileSaver.saveAs(new Blob([wbout], {type: 'application/octet-stream'}), '数量统计分析.xlsx')
                    ElMessage({message:'成功导出!',type:'success'})
                } catch (e) {
                    if (typeof console !== 'undefined') console.log(e, wbout)
                }
            }
            return {tableData,handleSizeChange,handleCurrentChange,page,exportExcel}
        }

    }
```

# element Tabs 用法,动态 增加标签,删除标签
## 特别注意:
- 书写 Vue组件文件名,定义的文件名,千万不能和内置标签重名,否则卡死,出错.莫名奇妙的错误...
```html
<template>
        <h2>Tabs测试</h2>
        <hr>
        <el-button type="success" @click="addonetab">增加一个标签</el-button>
        <el-tabs v-model="activeName"
                 class="demo-tabs"
                 type="card"
                 @tab-click="handleClick"
                 @edit="editTabs">

            <el-tab-pane label="用户" name="tabs_main">
                <!--首个标签页,不可删除-->
                <home></home>
            </el-tab-pane>
            <el-tab-pane v-for="(item,index) in selfdeftabs"
                         :key="index"
                         :name="item.name"
                         :label="item.title"
                         closable>
                <!--动态组件 显示位置.....重要-->
                <component :is="item.content"></component>
            </el-tab-pane>
        </el-tabs>
</template>
```
```javascript
<script>
    import {ref,reactive,shallowRef,defineAsyncComponent} from 'vue'
    import home from views
    export default {
        name:'MyElTabs',
        components:{
            home
        },

        setup(){
            const activeName = ref('tabs_main')
            const selfdeftabs=ref([])
            const handleClick = (tab, event) => {
                //console.log(tab, event)
            }

            let addonetab=()=>{
                let tabid=selfdeftabs.value.length+1
                let mtab='tab_'+tabid.toString()
                selfdeftabs.value.push({
                    name:mtab,
                    title:'自定义tab-'+tabid.toString(),
                    /**
                     * 重要!!!动态组件
                     */
                    content:shallowRef(defineAsyncComponent(()=>import(views+tabid.toString()+".vue")))
                })
                activeName.value=mtab
            }
            let editTabs=(targetName,actions)=>{
                console.log(targetName, actions)
                let tabs=selfdeftabs.value
                if (actions==='remove'){
                    selfdeftabs.value = tabs.filter((tab) => tab.name !== targetName)
                }

            }

            return {activeName,handleClick,addonetab,selfdeftabs,editTabs}
        }
    }
</script>

```