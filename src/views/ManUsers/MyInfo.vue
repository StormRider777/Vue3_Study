<template>
    <div>
        <div style="width:100%;display:flex;justify-content: space-around">
            <strong style="color:darkblue">我的详情</strong>
            <el-button @click="ExitOs" type="warning"><el-icon><Remove /></el-icon>退出系统</el-button>
        </div>
        <hr>
        <table width="90%">
            <tr style="height: 0.8rem"><td class="infolable">头像:</td>
                <td><img :src="userinfo.data.photo" alt=""
                         style="width: 0.75rem;height: 0.75rem;object-fit: cover;border-radius:25rem">
            </td></tr>
            <tr><td class="infolable">账号:</td><td><span v-text="userinfo.data.account"></span></td></tr>
            <tr><td class="infolable">注册时间:</td><td><span v-text="userinfo.data.createtime"></span></td></tr>
            <tr><td class="infolable">姓名:</td><td><el-input v-model="userinfo.data.name" :disabled="!userinfo.isEdit"></el-input></td></tr>
            <tr><td class="infolable">电话:</td><td><el-input v-model="userinfo.data.tele" :disabled="!userinfo.isEdit"></el-input></td></tr>
            <tr v-show="userinfo.isEdit"><td class="infolable"></td><td>
                <el-checkbox label="同时修改密码"  v-model="isEditPwd" style="font-size: 0.5rem"/>
            </td></tr>
            <tr v-show="isEditPwd && userinfo.isEdit"><td class="infolable">密码:</td><td><el-input v-model="userinfo.data.pwd" type="password" :disabled="!userinfo.isEdit"></el-input></td></tr>
            <tr v-show="isEditPwd && userinfo.isEdit"><td class="infolable">重复密码:</td><td><el-input v-model="userinfo.data.repwd" type="password" /></td></tr>
            <tr><td colspan="2" style="text-align: center;">
                <el-button :type="userinfo.isEdit?'success':'primary'" @click="userinfo.isEdit?UpdateUser('agree'):UpdateUser('edit')">
                    <span v-text="userinfo.isEdit?'确定':'修改'"></span>
                </el-button>
                <el-button type="success" v-show="userinfo.isEdit" @click="userinfo.isEdit=false"  style="margin-left: 0.3rem">
                    <span v-text="'取消'"></span>
                </el-button>
            </td></tr>
        </table>
        <hr>
        <div style="width: 100%;margin-left:8%;margin-top: 0.3rem">

            <el-button @click="gohelp" color="#8920aa"><el-icon><HelpFilled /></el-icon>操作指南</el-button>
        </div>
    </div>
</template>

<script>
    import {$get,$post} from "../../api/request"
    import {reactive,watch,ref,onMounted} from 'vue'
    import {useRouter} from 'vue-router'
    import {MM,GetStorageUserInfo} from '../../utils/MyUtils'
    import {useStore} from 'vuex'
    import {ElMessage} from 'element-plus'
    export default {
        name: "MyInfo",
        setup(){
            const isEditPwd=ref(false)
            var PWD=''
            const userinfo=reactive({isEdit:false,data:''})
            let router=useRouter()
            let store=useStore()

            watch(isEditPwd,(nv,ov)=>{
                if (nv){
                    userinfo.data.pwd=''
                    userinfo.data.repwd=''
                }else{
                    userinfo.data.pwd=PWD
                }
            })


            onMounted(()=>{
                let kw=store.state.logininfo.account

                $get('/jxc/getmyinfo/', {kw: kw}).then(res => {
                    if (res.data.res) {
                        // console.log(res.data.data)
                        userinfo.data = res.data.data
                        userinfo.data['repwd'] = userinfo.data.pwd
                        userinfo.data['createtime']=userinfo.data['createtime'].substr(0,19)
                        PWD = res.data.data.pwd
                        if (!userinfo.data.photo) {
                            userinfo.data.photo = '/dataserver/static/jxc/userphoto/default.jpg'
                        }
                    }
                })
            })



            let UpdateUser=(para)=>{
                if (para==='edit'){
                    userinfo.isEdit=true
                }else{
                    if (userinfo.isEdit){
                        if (validdata(userinfo.data)){
                            //console.log(isEditPwd.value,isEditPwd.value?MM(userinfo.data.pwd):userinfo.data.pwd,PWD)
                            let data={
                                account:userinfo.data.account,
                                name:userinfo.data.name,
                                tele:userinfo.data.tele,
                                pwd:isEditPwd.value?MM(userinfo.data.pwd):PWD,
                            }
                            $post('/jxc/updateuser/',data).then(res=>{
                                if (res.res){
                                    ElMessage({message:'修改成功:'+res.msg,type:'success',showClose:true})
                                    let logininfo=GetStorageUserInfo()
                                    logininfo.name=res.data.name
                                    logininfo.pwd=data.pwd
                                    localStorage.setItem('logininfo',
                                        JSON.stringify(logininfo)
                                    )
                                    store.commit('ChangeUser',{account:res.data.account,name:res.data.name,pwd:res.data.pwd})
                                    userinfo.isEdit=false
                                }else{
                                    ElMessage({message:'修改失败==>:'+res.msg,type:'error',showClose:true})
                                }
                            })
                        }
                    }
                }

            }

            let ExitOs=()=>{
                localStorage.clear()
                router.push('/login/')
            }
            let gohelp=()=>{
                router.push('/home/help/')
            }

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
                if (isEditPwd.value && data.pwd.length < 4) {
                    va = false
                    ElMessage({message: '密码必须大于4位!', type: 'error', showClose: true})
                }
                if (isEditPwd.value && data.pwd != data.repwd) {
                    va = false
                    ElMessage({message: '两次密码不一致!', type: 'error', showClose: true})
                }
                return va
            }
            return {userinfo,ExitOs,gohelp,UpdateUser,isEditPwd}
        }
    }

</script>

<style scoped>
    tr{
        height: 0.4rem;
    }
    .infolable{
        width: 0.9rem;
        text-align: right;
        padding-right: 0.1rem;
    }
</style>