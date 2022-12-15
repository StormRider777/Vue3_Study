<template>
    <div class="index">
        <el-button type="success" @click="about()">关于</el-button>
        <el-button type="primary"  @click="login()">登录</el-button>
        <el-button type="warning"  @click="home()">进入业务页面</el-button>
    </div>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "index",
        setup(){
            const router=useRouter()
            let about=()=>{
                router.push('/about/')
            }
            let login=()=>{
                router.push('/login/')
            }
            let home=()=>{
                router.push('/home/')
            }
            return {about,login,home}
        }
    }
</script>

<style scoped>
.index{
    width: 80%;
    margin: 80px auto;
    line-height: 50px;
    height: 50px;
    display: flex;
    justify-content:center;
    align-items: center;

}
.el-button{
    width: 200px;
    height: 45px;
}
</style>