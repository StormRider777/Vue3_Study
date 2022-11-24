<template>
    <div class="login">
        <span>登录页面</span>
        <hr>
        <table>
            <tr>
                <td style="width: 60px;text-align: right">用户名:</td>
                <td style="width: 200px;text-align: left">
                    <el-input v-model="user.name" placeholder="请输入用户名..." clearable />
                    <!--<input type="text" style="width: 90%" placeholder="请输入用户名..." autocomplete="off" required>-->
                </td>
            </tr>
            <tr><td style="text-align: right">密码: </td>
                <td style="width: 200px;text-align: left">
                     <el-input v-model="user.pwd" type="password" placeholder="请输入密码..." show-password/>
                    <!--<input type="password" style="width: 90%" placeholder="密码..." autocomplete="off">-->
                </td>
            </tr>
            <tr><td colspan="2" style="text-align: center">
                <el-button type="primary" :icon="Search" style="width:90%;height: 40px" @click="LoginSubmit()">登录</el-button>
                <!--<button style="width: 100%;height: 30px">登录</button>-->
            </td></tr>
        </table>
    </div>

</template>

<script>
    import { Search } from '@element-plus/icons-vue'
    import {reactive} from 'vue'
    import {useRouter} from 'vue-router'
    export default {
        name: "Login",
        setup(){
            const router=useRouter()
            function LoginSubmit() {
                alert('登录了')
                router.push('/home/')
            }

            const user= reactive({name:'',pwd:''})
            return {Search,user,LoginSubmit}
        }
    }
</script>

<style scoped>
    .login{
        border: 1px solid grey;
        width: 400px;
        height: 250px;
        margin: 100px auto;
    }
    tr{
        height: 55px;
    }
    table{
        margin: 15px auto;
        width: 300px;
    }
    /*input:focus{*/
        /*background: rgba(0,140,10,0.3);*/
        /*box-shadow: 0px 0px 4px 4px skyblue;*/
    /*}*/
</style>