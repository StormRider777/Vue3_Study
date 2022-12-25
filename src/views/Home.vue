<template>
    <el-container>
        <el-header>
            <comHeader></comHeader>
        </el-header>
        <el-main>
            <router-view v-slot="{ Component }">
                <transition name="aniview">
                    <component :is="Component"/>
                </transition>
            </router-view>
        </el-main>
        <el-footer>
            <comFooter></comFooter>
        </el-footer>
    </el-container>
</template>

<script>
    import comHeader from "../components/comHeader"
    import comFooter from "../components/comFooter"
    import {ref,reactive,onMounted} from 'vue'
    import {useRouter} from 'vue-router'
    import {ElMessage} from 'element-plus'
    import {$post} from '../api/request'
    export default {
        name: "Home",
        components:{
            comHeader,
            comFooter,
        },
        setup(){
            const router=useRouter()
            const LoginInfo=reactive({
                account:'',
                pwd:'',
                isLogin:false
            })
            onMounted(()=>{
                let login=localStorage.getItem('logininfo')
                // console.log('1',login)
                if (login){
                    // console.log('2',login)
                    login=JSON.parse(login)
                    if (login.hasOwnProperty('account') && login.hasOwnProperty('pwd')) {
                        LoginInfo.account = login.account
                        LoginInfo.pwd = login.pwd
                        $post('/jxc/login/', {account: LoginInfo.account, pwd: LoginInfo.pwd})
                            .then((res) => {
                                if (!res.res) {
                                    ElMessage({message: res.msg, type: 'error', showClose: true})
                                    router.push('/login/')
                                }
                            })
                    }else{
                        // console.log('0',login)
                        ElMessage({message:'请正确登录!', type: 'warning', showClose: true})
                        router.push('/login/')
                    }

                }else{
                    console.log('0',login)
                    ElMessage({message:'请正确登录!', type: 'warning', showClose: true})
                    router.push('/login/')
                }


            })
        }
    }
</script>

<style scoped>
    .el-container{
        width: 100%;
        height: 100%;
        padding: 0;
    }
    .el-header{
        height: .45rem;
        background: #2c3e50;
        margin: 0;
        padding: 0;
        line-height: .45rem;
        color:yellow;
    }
    .el-footer{
        height: .58rem;
        line-height: .58rem;
        padding: 0;
        margin: 0;

    }
    .el-main{
        overflow: auto;
    }
        .aniview-enter-from,.aniview-leave-to{
        position: absolute;
        left:10%;
        top: .7rem;
        transform: translateX(100%);
        opacity: 0;
    }
    .aniview-enter-to,.aniview-leave-from{
        transform: translateX(0);
        opacity: 1;
    }
    .aniview-enter-active,.aniview-leave-active {
        transition: all 0.5s
    }
</style>