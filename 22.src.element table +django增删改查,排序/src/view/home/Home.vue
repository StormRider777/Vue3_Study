<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <el-row :gutter="30">
                    <el-col :span="15" style="padding-left: 10px;color:darkblue;font-size: 25px">
                        <strong v-text="baseinfo.osname"></strong>
                    </el-col>
                    <el-col :span="3" style="text-align: right;color:snow">
                        当前用户:
                    </el-col>
                    <el-col :span="3" style="text-align: left;padding-left: 10px;color:yellow">
                        <span v-text="baseinfo.user.name"></span>
                    </el-col>
                    <el-col :span="3" style="text-align: right">
                        <el-button type="warning" @click="exitbtn()">
                            <el-icon><SwitchButton /></el-icon>
                            退出系统
                        </el-button>
                    </el-col>

                </el-row>
            </el-header>

            <el-container>
                <el-aside width="220px">
                    <Menus></Menus>
                </el-aside>
                <el-main>
                    <router-view v-slot="{ Component }">
                        <transition name="aniview">
                            <component :is="Component" />
                        </transition>
                    </router-view>
                </el-main>
            </el-container>
            <el-footer>
                <span v-text="baseinfo.dwname"></span>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    import {reactive,onMounted} from 'vue'
    import {useRouter} from 'vue-router'
    import {ElMessageBox} from 'element-plus'
    import {useStore} from 'vuex'
    import Menus from "./Menus"
    export default {
        name: "Home",
        components:{Menus},
        setup(){
            const router=useRouter()
            const store=useStore()


            var user={
                name:'',
                pwd:''
            }

            var userinfo=localStorage.hasOwnProperty('loginuser')
            if (userinfo){
                userinfo=window.localStorage.getItem('loginuser')
                userinfo=JSON.parse(userinfo)
                user.name=userinfo.name
                user.pwd=userinfo.pwd
            }
            if (user.name && user.pwd){
                //为真
            } else{
                ElMessageBox({
                    title:'提示',
                    message:`当前用户非法,<strong style="color:red">使用Test测试用户登录!</strong>`,
                    distinguishCancelAndClose: true,
                    dangerouslyUseHTMLString: true,
                    closeOnClickModal:false,
                }).then(()=>{
                    // 使用Test测试账号登录
                    userinfo={name:"Test",pwd:'0000'}
                    localStorage.setItem('loginuser',JSON.stringify(userinfo))
                    router.push('/home')
                }).catch((e)=>{

                })
            }
            const baseinfo=reactive({
                osname: store.state.osinfo.osname,
                dwname: store.state.osinfo.dwname,
                user:{
                    name:user.name,
                    pwd:user.pwd
                }
            })

            function exitbtn() {
                ElMessageBox.confirm(
                    `尊敬的: <strong style="color: red">  ${baseinfo.user.name} </strong> 退出系统!`,
                    '退出系统',
                    {
                        dangerouslyUseHTMLString:true,
                        cancelButtonText:'不退出',
                        confirmButtonText: '退出',
                        type:'warning',
                        draggable: true,

                }).then((e)=>{
                    window.localStorage.removeItem('loginuser')
                    //console.log(e,typeof(e))
                    router.push('/')
                }).catch((e)=>{
                    //console.log(e,typeof(e))
                })
            }

            return {baseinfo,exitbtn}
        }
    }
</script>

<style scoped>
    .el-container,.common-layout{
        width: 100%;
        height: 100%;
        overflow: hidden;
    }

    .el-header{
        background: linear-gradient(to right,skyblue,deepskyblue,dodgerblue,blue,darkblue);
        height: 50px;
        line-height: 50px;
        padding-left: 10px;
    }
    .el-footer{
        background: slategray;
        color:whitesmoke;
        text-align: center;
        height: 40px;
        line-height: 40px;
    }
    .el-aside{
        background: #545c64;
        height: 100%;
    }
    .el-main{
        background: snow;
        overflow: hidden;
    }
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
</style>