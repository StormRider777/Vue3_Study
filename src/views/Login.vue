<template>
    <table width="90%" STYLE="margin: 1rem auto">
        <tr style="height: 1rem">
            <td style="text-align: center">
                <img src="../assets/logo.png"  style="width: 1rem;height: 1rem" alt="">
            </td>
        </tr>
        <tr>
            <td>
                <el-input v-model="userinfo.account" placeholder="请输入账号...">
                    <template #prepend>账号:</template>
                    <template  #append>
                        <el-icon><UserFilled /></el-icon>
                    </template>
                </el-input>
            </td>
        </tr>
        <tr>
            <td>
                <el-input v-model="userinfo.pwd" placeholder="请输入密码..." type="password">
                    <template #prepend>密码:</template>
                    <template  #append>
                        <el-icon><Lock /></el-icon>
                    </template>
                </el-input>
            </td>
        </tr>
        <tr>
            <td style="padding-left: 0.5rem">
                <el-checkbox label="记住我"  v-model="userinfo.autologinck" style="font-size: 0.5rem"/>
            </td>
        </tr>

        <tr>
            <td>
                <el-button type="success" @click="toLogin(false)">
                    <el-icon size="0.2rem" color="red"><CircleCheck /></el-icon>&nbsp;
                    <strong style="font-size: 0.2rem">登 录</strong>
                </el-button>
            </td>
        </tr>
    </table>
</template>

<script>
    import {useRouter} from 'vue-router'
    import {reactive,onMounted} from 'vue'
    import {$post} from "../api/request"
    import {MM,GetStorageUserInfo} from "../utils/MyUtils"
    import {ElMessage} from "element-plus"
    import {useStore} from 'vuex'
    export default {
        name: "Login",
        setup(){
            const userinfo=reactive({
                account:'',
                pwd:'',
                autologinck:false
            })
            let router=useRouter()
            let store=useStore()
            let toLogin=(isAutoLogin=false)=>{
                 //console.log(isAutoLogin,{account:userinfo.account,pwd:isAutoLogin ? userinfo.pwd:MyUtils(userinfo.pwd)})
                $post('/jxc/login/',{account:userinfo.account,pwd:isAutoLogin ? userinfo.pwd:MM(userinfo.pwd)})
                    .then((res)=>{
                        if (res.res) {
                            //console.log(res.data)
                            ElMessage({message: res.msg, type: 'success', showClose: true})
                            localStorage.setItem('logininfo',
                                JSON.stringify({
                                    account:res.data.account,
                                    pwd: res.data.pwd,
                                    autologinck: userinfo.autologinck,
                                    name:res.data.name
                                })
                            )
                            store.commit('ChangeUser',{account:res.data.account,name:res.data.name,pwd:res.data.pwd})
                            router.push('/home/')
                        } else {
                            localStorage.setItem('logininfo', JSON.stringify({account:'', pwd: '', autologinck: false,name:''}))
                            ElMessage({message: res.msg, type: 'error', showClose: true})
                        }
                })
            }

            onMounted(()=>{
                let logininfo=GetStorageUserInfo()
                //console.log(logininfo)
                if (logininfo.autologinck){
                    userinfo.account=logininfo.account
                    userinfo.pwd=logininfo.pwd
                    userinfo.autologinck=logininfo.autologinck
                    toLogin(true)
                }
            })

            return {userinfo,toLogin}
        }
    }
</script>

<style scoped>
    tr{
        height: 0.6rem;
    }
   td>.el-button{
       width: 100%;
       height: 0.5rem;
   }
    .el-input{
        height: 0.45rem;
        font-size: 0.18rem;
    }
    :deep(.el-checkbox__label){
        font-size: 0.17rem;
        color:seagreen;
    }

</style>