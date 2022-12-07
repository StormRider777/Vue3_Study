<template>
    <div style="background: snow;width: 300px;height: 250px;margin: 10px auto;border: 1px solid grey;border-radius:5px;box-shadow: 0px 0px 2px 2px gray">
        <div style="height: 40px;line-height: 40px;padding-left: 10px;color:darkblue;;border-bottom: 1px solid pink;text-align: left">
            请登陆
        </div>
        <table width="100%">
                <!--border="1" cellspacing="0" cellpadding="0" style="border-color: green;border-collapse: collapse"-->
            <tr>
                <td class="cpation">用户名:</td>
                <td><input type="text" v-model="logininfo.name"></td>
            </tr>
            <tr>
                <td class="cpation">密码:</td>
                <td><input type="password" v-model="logininfo.pwd"></td>
            </tr>
            <tr>
                <td colspan="2">
                    <button @click="submit">登录</button>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <span v-show="logininfo.islogin" v-text="logininfo.loginres" style="color: red"></span>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
    import login from '../hooks/login_hook'
    import {onMounted,reactive} from 'vue'
    import axios from 'axios'
    export default {
        name: "MyPage",
        setup(){
            let csrf_token=''
            let logininfo=reactive({
                name:'StormRider',
                pwd:'1234567',
                islogin:false,
                loginres:{},
            })
            onMounted(()=>{
                axios.get('/api/getcsrf/').then((res)=>{
                    csrf_token=res.data.csrf_token
                    document.cookie="csrftoken="+csrf_token
                })
            })
            function  submit() {
                //login(logininfo.name,logininfo.pwd)
                login(logininfo.name,logininfo.pwd).then((res)=>{
                    logininfo.loginres=res.data
                    logininfo.islogin=true
                    console.log('res------:',logininfo.loginres)
                })

            }
            return {
                logininfo,
                submit
            }
        }


    }
</script>

<style scoped>
    .cpation{
        text-align: right;
        width:80px
    }
    tr{
        height: 50px;
    }
    input{
        height: 25px;
        width: 80%;
    }
    input:hover{
        border-color: grey;
        box-shadow: 0px 0px 3px 3px skyblue;
        border-color: grey;
    }
    button{
        height: 40px;
        width: 200px;
    }

</style>