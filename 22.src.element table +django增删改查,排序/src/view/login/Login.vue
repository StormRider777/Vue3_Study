<template>
    <div class="pagediv">
        <div class="logindiv">
            <span>系统登录</span>
            <hr>
            <table>
                <tr>
                    <td class="inputlabel">用户名:</td>
                    <td class="inputdata">
                        <el-input v-model="user.name" placeholder="请输入用户名..." required clearable>
                            <template #append><el-icon><UserFilled /></el-icon></template>
                        </el-input>
                    </td>
                </tr>
                <tr>
                    <td class="inputlabel">密码:</td>
                    <td class="inputdata">
                        <el-input v-model="user.pwd" type="password" placeholder="输入密码..." show-password require clearable>
                            <template #append><el-icon><Lock /></el-icon></template>
                        </el-input>
                    </td>
                </tr>
                <tr>
                    <td colspan="2" style="text-align: center">
                        <el-button type="success" @click="submitbtn()" style="width: 100%;margin: 20px auto;height: 35px">
                            <el-icon><SuccessFilled /></el-icon>
                            提交
                        </el-button>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
    import {reactive,onMounted} from 'vue'
    import { ElMessage, ElMessageBox } from 'element-plus'
    import {useRouter} from 'vue-router'
    // import type { Action } from 'element-plus'
    import {useStore} from 'vuex'
    import GetDatas from "../../hook/GetDatas"
    import axios from 'axios'
    import $ from '../../../public/jquery.min'
    export default {
        name: "Login",
        setup(){
            const store=reactive(useStore())
            const router=useRouter()
            /*
            * 此处 测试用登录用户数据
            * */
            const user=reactive({
                name:'0001',
                //store.state.osinfo.user.name,
                pwd:'0000',
            //store.state.osinfo.user.pwd
            })
            var DataServer=store.state.osinfo.datapath.login

                //store.state.osinfo.datapath.gettoken.path
            onMounted(()=>{
                // axios({
                //     method:'get',
                //     url:`/dataserver/${Tokenpath}`
                // }).then((res)=>{
                //     store.commit('updatetoken',res.data)
                // }).catch((err)=>{
                //     ElMessageBox({
                //         title:'提示',
                //         message: `<strong style="color:red"> 未获得后端数据通讯服务的令牌! </strong> ，请确认端服务器状态!`,
                //         dangerouslyUseHTMLString: true,
                //         confirmButtonText: '确认',
                //         closeOnClickModal:false,
                //         center:true,
                //     })
                // })
            })
            /*
            * 正常情况下,输入数据后 axios 到服务器数据库去验证
            * */

            function getCookie(c_name){
                if (document.cookie.length>0){　　//先查询cookie是否为空，为空就return ""
                    let c_start=document.cookie.indexOf(c_name + "=")　　//通过String对象的indexOf()来检查这个cookie是否存在，不存在就为 -1　　
                    if (c_start!=-1){
                        c_start=c_start + c_name.length+1　　//最后这个+1其实就是表示"="号啦，这样就获取到了cookie值的开始位置
                        let c_end=document.cookie.indexOf(";",c_start)　　//其实我刚看见indexOf()第二个参数的时候猛然有点晕，后来想起来表示指定的开始索引的位置...这句是为了得到值的结束位置。因为需要考虑是否是最后一项，所以通过";"号是否存在来判断
                        if (c_end==-1) c_end=document.cookie.length　　
                        return unescape(document.cookie.substring(c_start,c_end))　　//通过substring()得到了值。想了解unescape()得先知道escape()是做什么的，都是很重要的基础，想了解的可以搜索下，在文章结尾处也会进行讲解cookie编码细节
                    }
                }
                return ""
            }

            function submitbtn(){
                /*
                *
                * */
                let data=new FormData()
                data.append('name',user.name)
                data.append('pwd',user.pwd)

                let url=`/dataserver/${store.state.osinfo.datapath.login.path}`
                let tokenpath=store.state.osinfo.datapath.gettoken.path

                let token=GetDatas.gettoken(`/dataserver/${tokenpath}`)
                //let token=getCookie('csrftoken')
                data.append('csrfmiddlewaretoken',token)
                //console.log('token:',token)
                /* 使用 XHR 发送
                let xhr=new XMLHttpRequest()
                xhr.open('POST',url,false)
                xhr.setRequestHeader('X-CSRFToken',token)
                xhr.send(data)
                console.log(xhr.responseText)
                */
                /* 使用jquery $.ajax 发送
                $.ajax({
                    url:url,
                    type:'post',
                    data:{name:'0001',pwd:'0000',csrfmiddlewaretoken:token},
                    success:function (res) {
                        console.log(res)
                    }
                })
                */
                /*使用axios发送*/
                axios({
                    method:'post',
                    url,
                    data,
                    headers: {'X-CSRFToken': token}  //一直没有完美解决 vue 与后端django 的csrf 验证失败问题.无解.....!
                }).then((res)=>{
                    let loginuser=res.data
                    if (loginuser.name){
                        window.localStorage.setItem('loginuser',JSON.stringify(loginuser))
                        router.push('/home/')
                    }else{
                        ElMessageBox.alert(
                            `<strong style="color: red">用户名或密码错误错误,请重新输入!</strong>`,
                            '提示',
                            {
                            confirmButtonText: '确认',
                            closeOnClickModal:false,
                            dangerouslyUseHTMLString: true,
                        })
                    }

                }).catch((err)=>{
                    ElMessageBox.alert(
                        `<strong style="color: red">${err.message}</strong>`,
                        '登录失败',
                        {
                        confirmButtonText: '确认',
                        closeOnClickModal:false,
                        dangerouslyUseHTMLString: true,
                    })
                })


                /*
                ElMessageBox.confirm(
                    `当前登录用户: <strong style="color: red">${user.name} </strong>, 请确认是否登录到主页?`,
                    '是否登录?',
                {
                    distinguishCancelAndClose: true,
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    closeOnClickModal:false,
                    center:true,
                    dangerouslyUseHTMLString: true,
                })
                .then(() => {
                    ElMessageBox({
                        //type: 'info',
                        title:'提示',
                        message: `尊敬的:<strong style="color:red"> ${user.name} </strong> ，您确认了登录主页!`,
                        dangerouslyUseHTMLString: true,
                    }).then(()=>{
                        const UserInfo=JSON.stringify({name:user.name,pwd:user.pwd})
                        window.localStorage.setItem('loginuser',UserInfo)
                        router.push('/home')
                    })
                })
                .catch((action) => {
                    ElMessage({
                        type: 'info',
                        message:action === 'cancel'? '取消了登录!' : '返回登录页',
                    })

                })*/
            }
            return {user,submitbtn}
        }
    }
</script>

<style scoped>
    .pagediv{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(to bottom, skyblue, deepskyblue, dodgerblue, blue,midnightblue,darkblue);
    }
    .logindiv{
        border: 1px solid grey;
        border-radius: 5px;
        width: 400px;
        height: 230px;
        padding: 5px 5px 5px 5px;
        margin: 180px auto;
        background: snow;
    }
    table{
        width:80%;
        margin: 20px auto;
    }
    tr{
        height: 45px;
    }
    .inputlabel{
        width: 80px;
        padding-right: 5px;
        text-align: right;
    }
    .inputdata{
        padding-left: 5px;
        text-align: left;
    }
</style>