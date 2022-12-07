<template>
    <div class="logindiv">
        <table>
            <tr><td colspan="2"><div class="logintitle">系统登录</div></td></tr>
            <tr style="height: 10px"><td></td></tr>
            <tr>
                <td class="labelarea">账号:</td>
                <td class="inputarea">
                    <el-input v-model="loginuser.username" clearable placehodler="'请输入登录账号...">
                        <template #append><el-icon><UserFilled /></el-icon></template>
                    </el-input>
                </td></tr>
            <tr>
                <td class="labelarea">密码:</td>
                <td class="inputarea">
                    <el-input type="password" v-model="loginuser.userpwd" clearable placehodler="'请输入登录密码...">
                        <template #append><el-icon><Lock /></el-icon></template>
                    </el-input>
                </td></tr>
             <tr>
                <td class="labelarea">记住我:</td>
                <td class="inputarea">
                    <el-checkbox v-model="loginuser.rememberme" clearable placehodler="'请输入登录密码..." />

                </td></tr>
            <tr style="height: 10px"><td></td></tr>
            <tr><td colspan="2" style="text-align: center"><el-button type="success" @click="login">登录</el-button></td></tr>
        </table>
    </div>
</template>

<script>
    import {useStore} from "vuex"
    import {reactive} from 'vue'
    import {Login} from "../apiURL/api"
    import {useRouter} from 'vue-router'
    import {ElMessage,ElMessageBox} from 'element-plus'
    export default {
        name: "Login",
        setup(){
            const router=useRouter()
            const store=useStore()
            const loginuser=reactive({
                username:'005',
                userpwd:'1234',
                usertoken:'',
                rememberme:false,
            })
            //console.log(store.state.config.type)

            function login() {
                Login({name:loginuser.username,pwd:loginuser.userpwd,csrfmiddlewaretoken:store.state.config.Token}).then(r=>{
                    if (r.data.res){
                        let user={name:loginuser.username,pwd:loginuser.userpwd,rememberme:loginuser.rememberme}
                        ElMessage({message:'登录成功!'+r.data.result.name,type:'success'})
                        store.commit('config/saveToken',r.data)
                        store.commit('config/UpdateUser',user)
                        localStorage.setItem('loginuserinfo',JSON.stringify(user))
                        router.push('/home/')
                    }else{
                        ElMessageBox({
                            message:'登录失败:'+r.data.msg,
                            title:'登录失败',
                            type:'error'
                        })
                    }
                }).catch(e=>{
                    ElMessageBox({
                        message:'登录失败:'+e.message,
                        title:'登录失败!',
                        type:'warning'
                    })
                    router.push('/login/')
                })
                //loginXHR()
            }
            function loginXHR() {
                let data=new FormData()
                data.append('name',loginuser.username)
                data.append('pwd',loginuser.userpwd)

                let xhr = new XMLHttpRequest()
                xhr.open('POST','/dataserver/data/login/',false)
                xhr.setRequestHeader('X-CSRFToken',store.state.config.Token)
                xhr.send()
                console.log('XHR:',xhr.responseText)
            }

            return {loginuser,login}
        }
    }
</script>

<style scoped>
    tr{
        height: 40px;
    }
    .logindiv{
        width:400px;
        height: 250px;
        border: 1px solid lightgrey;
        border-radius: 5px;
        background: ghostwhite;
        margin: 100px auto;
        padding: 10px 10px;
    }
    table{
        width: 100%;
    }
    td{
        padding-left:10px ;
        padding-right: 10px;
    }
    .labelarea{
        text-align: right;
        width: 60px;
    }
    .inputarea{
        text-align: left;
    }
    .el-button{
        width: 90%;
        height: 38px;
    }
    .logintitle{
        border-bottom: 1px solid gray;
        width: 100%;
        line-height: 45px;
        font-size: 20px;
    }
</style>