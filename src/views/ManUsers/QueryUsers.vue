<template>
    <div style="margin: 0 auto;width: 100%;height: 100%;">
        <el-row>
            <el-col :span="6">
                <el-button type="success" style="width: 0.9rem" @click="handleAdd"> <el-icon><Plus /></el-icon>增加用户</el-button>
            </el-col>

            <el-col :span="15" :offset="2">
                <el-input v-model="searchkw" placeholder="查询关键字...">
                    <template #append>
                        <el-button @click="QueryUser">
                            <el-icon><Search /></el-icon>查询
                        </el-button>
                    </template>
                </el-input>
            </el-col>
        </el-row>
        <el-table :data="userinfotable.data" border style="width: 100%;margin: 0.05rem auto">
            <!--<el-table-column prop="photo" label="头像" />-->
            <el-table-column prop="account" label="账号" width="100"/>
            <el-table-column prop="name" label="姓名" width="120"/>
            <!--<el-table-column prop="tele" label="电话" />-->
            <!--<el-table-column prop="createtime" label="注册时间" />-->
            <el-table-column label="操作" align="center">
                <template #default="scope">
                    <el-button type="warning" @click="handleDetail(scope.$index, scope.row)" >详情</el-button>
                    <el-button  type="primary" @click="handleEdit(scope.$index, scope.row)">修改</el-button>
                    <el-button  type="danger" @click="handleDelete(scope.$index, scope.row)" v-show="scope.row.account!='admin'">删除</el-button>
                </template>
            </el-table-column>
        </el-table>

        <el-drawer v-model="DialogCurrentState.display"
                   direction="rtl"
                   :before-close="handleClose"
                   :close-on-click-modal="false"
                   size="90%"
                   style="height: 85%;margin-top: 0.5rem;padding-top: 0">
            <template #header>
                <span v-text="DialogCurrentState.title" ></span>
            </template>
            <template #default>
                <table width="100%" style="margin: 0 auto">
                    <tr>
                        <td class="tdlabel">头像:</td>
                        <td style="display: grid;justify-items: left">
                            <el-image style="width: 0.75rem;height: 0.75rem;object-fit: cover;border-radius:25rem"
                                      :src="DialogCurrentState.data.photo" fit="cover" />
                             <el-button type="success" style="margin-left: 0.08rem;width: 0.75rem;margin-top: 0.05rem;"
                                        :disabled="true || DialogCurrentState.isEdit">
                                 上传图片
                             </el-button>
                        </td>
                    </tr>
                    <tr><td class="tdlabel">注册时间:</td><td><span v-text="DialogCurrentState.data.createtime"></span></td></tr>
                    <tr>
                        <td class="tdlabel">账号:</td>
                        <td><el-input v-model="DialogCurrentState.data.account" :disabled="DialogCurrentStateName!='Add'" ></el-input></td>
                    </tr>

                    <tr>
                        <td class="tdlabel">姓名:</td>
                        <td><el-input class='inputname' v-model="DialogCurrentState.data.name" :disabled="DialogCurrentState.isEdit"></el-input></td>
                    </tr>
                    <tr>
                        <td class="tdlabel">电话:</td>
                        <td><el-input v-model="DialogCurrentState.data.tele" :disabled="DialogCurrentState.isEdit"></el-input></td>
                    </tr>
                    <tr>
                        <td class="tdlabel">密码:</td>
                        <td style="display: flex;justify-content: left">
                            <el-input type="password" v-model="DialogCurrentState.data.pwd" :disabled="true"></el-input>
                            <el-button type="success" style="margin-left: 0.08rem"
                                       :disabled="DialogCurrentState.isEdit"
                                       v-show="DialogCurrentStateName=='Edit'"
                                       @click="ChangePwdDialog=true">
                                修改密码
                            </el-button>
                            <span v-text="'新增用户的默认密码 0000'" v-show="DialogCurrentStateName=='Add'" style="font-size: 0.12rem;color:red"></span>
                        </td>
                    </tr>
                </table>
            </template>
            <template #footer>
                <div style="display: flex;justify-content: center;width: 100%">
                    <el-button type="warning" style="width: 1.2rem;height: 0.35rem" @click="btnCloseDialog">返回</el-button>
                    <el-button type="success" style="width: 1.2rem;height: 0.35rem;margin-left: 0.3rem" @click="btnCloseDialogYes">确定</el-button>
                </div>
            </template>
        </el-drawer>

        <el-dialog v-model="ChangePwdDialog" title='修改密码'
                   :close-on-click-modal="false"
                   width="90%" >
            <div>原密码</div>
            <el-input type="password" v-model="changepwd.oldpwd"></el-input>
            <div style="margin-top: 0.15rem;width: 100%">新密码:</div>
            <el-input type="password" v-model="changepwd.newpwd"></el-input>
            <div style="margin-top: 0.15rem;width: 100%">再一次:</div>
            <el-input type="password" v-model="changepwd.repwd"></el-input>
            <div style="text-align: center;width: 100%;margin-top: 0.2rem">
                <el-button type="primary" @click="ChangePwd" style="width: 90%;margin: 0.2rem auto">
                    <el-icon><Check /></el-icon>
                    确定修改
                </el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {ref,reactive,onMounted,markRaw} from 'vue'
    import {$get,$post} from "../../api/request"
    import {ElMessage,ElMessageBox} from 'element-plus'
    import {MM} from "../../utils/MyUtils"
    export default {
        name: "QueryUsers",
        setup(){

            let searchkw=ref('')
            let DialogStates={
                default:{display:false,title:'浏览-隐藏显示',isEdit:false,index:null,data:{}},
                detail:{display:true,title:'用户详情',isEdit:true,index:null,data:{}},
                edit:{display:true,title:'修改用户',isEdit:false,index:null,data:{}},
                add:{display:true,title:'增加用户',isEdit:false,index:null,data:{id:'',name:'',account:'',tele:'',photo:'',pwd:'',createtime:''}},
                dele:{display:true,title:'确认删除',isEdit:true,index:null,data:{}},
            }  //nomarl 浏览 add 新增 edit 修改 dele 删除

            let DialogCurrentState=ref(DialogStates.default)
            let DialogCurrentStateName=ref('')

            //表格数据
            let userinfotable=reactive({
                data:[{id:null,name:null,account:null,tele:null,createtime:null,photo:null}]
            })

            let ChangePwdDialog=ref(false)
            const changepwd=reactive({
                oldpwd:'',
                newpwd:'',
                repwd:''
            })

            //挂载,加载数据mok
            onMounted(()=>{
                $get('/jxc/getuserslist/',{kw:''}).then(res=>{
                    //console.log(res.data)
                    userinfotable.data=res.data.data
                })
            })

            // 查询详情 ,ok
            let handleDetail=(index,row)=>{
                if (!row.photo){
                    row.photo='/dataserver/static/jxc/userphoto/default.jpg'
                }
                DialogStates.detail.data=row
                DialogStates.detail.index=index
                DialogStates.detail.data['createtime']=DialogStates.detail.data['createtime'].substring(0,19)
                DialogCurrentState.value=DialogStates.detail
                DialogCurrentStateName.value='Detail'
            }

            //点击删除按钮 ok
            let handleDelete=(index,row)=>{
                DialogStates.dele.data=row
                DialogStates.dele.index=index
                DialogCurrentState.value=DialogStates.dele
                DialogStates.dele.data['createtime']=DialogStates.dele.data['createtime'].substring(0,19)
                DialogCurrentStateName.value='Dele'

            }
            //点击编辑按钮 ok
            let handleEdit=(index,row)=>{
                DialogStates.edit.data=row
                DialogStates.edit.index=index
                DialogCurrentState.value=DialogStates.edit
                changepwd.olpwd=''
                changepwd.newpwd=''
                changepwd.repwd=''
                DialogStates.edit.data['createtime']=DialogStates.edit.data['createtime'].substring(0,19)
                DialogCurrentStateName.value='Edit'
            }
            //点击增加按钮  ok
            let handleAdd=()=>{
                DialogCurrentState.value=DialogStates.add
                DialogCurrentStateName.value='Add'
            }

            //关闭对话框触发时间,恢复默认状态,不是增删改查, ok
            let handleClose=(done)=>{
                DialogCurrentState.value=DialogStates.default
                done()
                // console.log('close',DialogCurrentState.value)
            }

            //手动关闭抽屉对话框 ok
            let btnCloseDialog=()=>{
                DialogCurrentState.value=DialogStates.default
                DialogCurrentStateName.value=''
            }

            //点击对话框中的确认按钮,ok
            let btnCloseDialogYes=()=>{
                let op=DialogCurrentStateName.value
                let data={
                    id:DialogCurrentState.value.data.id,
                    account:DialogCurrentState.value.data.account,
                    name:DialogCurrentState.value.data.name,
                    tele:DialogCurrentState.value.data.tele,
                    pwd:DialogCurrentState.value.data.pwd,
                    photo:'',
                }
                //修改 ok
                if (op==='Edit'){
                    if (validdata(data)){
                        $post('/jxc/updateuser/', data).then(res => {
                            if (res.res) {
                                ElMessage({message: res.msg, type: 'success', showClose: true})
                            } else {
                                ElMessage({message: res.msg, type: 'error', showClose: true})
                            }
                        })
                    }

                }
                //删除 ok
                if (op==='Dele'){
                    ElMessageBox({
                        title:'确定删除吗?',
                        confirmButtonText: '删除',
                        cancelButtonText: '取消',
                        message:`确定删除:<br><strong style="color:red;margin-left: 0.5rem">${data.account}</strong><br><strong style="margin-left: 0.5rem;color:red">${data.name}</strong>`,
                        dangerouslyUseHTMLString: true,
                    }).then(res=>{
                        $post('/jxc/deleuser/',data).then(res=>{
                            if (res.res){
                                userinfotable.data.splice(DialogStates.dele.index,1)
                                ElMessage({message:res.msg,type:'success',showClose:true})
                            }else{
                                ElMessage({message:res.msg,type:'error',showClose:true})
                            }
                        })
                    }).catch(()=>{
                    })
                }

                //增加.ok
                if (op==='Add'){
                    data.pwd=MM('0000')
                    //console.log(data)
                    if (validdata(data)){
                        $post('/jxc/adduser/',data).then(res=>{
                            if (res.res){
                                ElMessage({message:res.msg,type:'success',showClose:true})
                                userinfotable.data.unshift(res.data)
                            }else{
                                ElMessage({message:res.msg,type:'error',showClose:true})
                            }
                        })
                        // # method:POST [name,pwd,repwd,account,tele,photo,FILES]
                    }else{
                        return false
                    }
                }
                DialogCurrentState.value=DialogStates.default
                DialogCurrentStateName.value=''
            }

            //修改密码 ok
            let ChangePwd=()=>{
                var va=true
                if (changepwd.newpwd!=changepwd.repwd){
                    ElMessage({message:'两次新密码不一致',type:'error',showClose:true})
                    va=false
                    return false
                }
                if (changepwd.newpwd.length<6){
                    ElMessage({message:'密码不能小于6位',type:'error',showClose:true})
                    va=false
                    return false
                }

                if (va){
                    const data={
                        account:DialogCurrentState.value.data.account,
                        newpwd:MM(changepwd.newpwd),
                        oldpwd:MM(changepwd.oldpwd)
                    }
                    $post('/jxc/changepwd/',data).then(res=>{
                        if (res.res){
                            ElMessage({message:res.msg,type:'success',showClose:true})
                        }else{
                            ElMessage({message:res.msg,type:'error',showClose:true})
                        }
                    })
                }
                    // ?account=xxxx
                    // # method :POST  account
            }

            //模糊查询 kw

            let QueryUser=()=>{
                $get('/jxc/getuserslist/',{kw:searchkw.value}).then(res=>{
                    //console.log(res.data)
                    userinfotable.data=res.data.data
                })
            }
            //数据校验 ok
            function validdata(data){
                let va = true
                if (data.name.length < 1) {
                    va = false
                    ElMessage({message: '姓名不能为空!', type: 'error', showClose: true})
                }
                if (data.account.length < 4) {
                    va = false
                    ElMessage({message: '账号长度必须大于4位!', type: 'error', showClose: true})
                }
                return va
            }
            return {
                DialogCurrentState,DialogCurrentStateName,searchkw,userinfotable,ChangePwdDialog,changepwd,
                handleClose,btnCloseDialog,handleAdd,btnCloseDialogYes,ChangePwd,QueryUser,
                handleDetail,handleDelete,handleEdit
            }
        }

    }
</script>

<style  scoped>
    .el-table .el-button{
        margin: 0.07rem auto;
        margin-left: 0.05rem;
        width: 1rem;
    }
    tr{
        height: 0.45rem;
    }
    .tdlabel{
        width: 0.9rem;
        text-align: right;
    }

</style>