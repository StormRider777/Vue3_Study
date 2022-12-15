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
                <el-aside width="200px">Aside</el-aside>
                <el-main>Main</el-main>
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
    export default {
        name: "Home",
        setup(){
            const router=useRouter()
            const store=useStore()
            var userinfo=window.localStorage.getItem('loginuser','{}')
            var user={
                name:'',
                pwd:''
            }
            userinfo=JSON.parse(userinfo)
            if (userinfo.hasOwnProperty('name') && userinfo.hasOwnProperty('pwd')){
                user.name=userinfo.name
                user.pwd=userinfo.pwd
            }
            if (user.name && user.pwd){
                //为真
            } else{
                ElMessageBox({
                    title:'提示',
                    message:`当前用户非法,<strong style="color:red">不允许登录!</strong>`,
                    distinguishCancelAndClose: true,
                    dangerouslyUseHTMLString: true,
                    closeOnClickModal:false,
                }).then(()=>{
                    router.push('/')
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
                    window.localStorage.setItem('loginuser',JSON.stringify({}))
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
        background: lightgray;
    }
    .el-main{
        background: snow;
    }
</style>