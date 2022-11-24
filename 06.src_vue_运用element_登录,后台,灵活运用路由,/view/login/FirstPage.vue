<template>
    <el-container style="text-align: center;height:40px;margin: 50px auto;min-width: 800px">
        <el-row>
            <el-col :span="6"></el-col>
            <el-col :span="4"><el-button @click="toabout" type="success">关于</el-button></el-col>
            <el-col :span="4"><el-button @click="tologin" type="primary">登录</el-button></el-col>
            <el-col :span="4"><el-button @click="tohome" type="warning">主页</el-button></el-col>
            <el-col :span="6"></el-col>
        </el-row>
    </el-container>


</template>

<script>
    import {useRouter} from 'vue-router'
    import {ref} from 'vue'

    export default {
        name: "App",
        setup(){
            const router=useRouter()
            const status=ref('')
            function tologin() {
                status.value='已经点击登录按钮！'
                router.replace('/login/')
            }
            function tohome() {
                status.value='已经点击主页按钮！'
                router.push('/home/')
            }
            function toabout() {
                status.value='已经关于按钮！'
                router.push('/about/')
            }

            return {tologin,status,tohome,toabout}
        }
    }
</script>

<style scoped>
    .el-row{
        height: 100%;
        width: 100%;
    }
    .el-col{
        padding-left: 10px;
        padding-left: 10px;
    }
    button{
        height: 100%;
        width: 100%;
    }
</style>