<template>
    <el-container>
        <el-row>
            <el-col :span="6"></el-col>
            <el-col :span="3">
                <el-button type="primary" style="width: 90%;height: 50px" @click="tologin()">
                    <el-icon><User /></el-icon>
                    系统登录
                </el-button>
            </el-col>
            <el-col :span="3">
                <el-button type="success" style="width: 90%;height: 50px" @click="tohome">
                    <el-icon><House /></el-icon>
                    后台主页
                </el-button>
            </el-col>
            <el-col :span="3">
                <el-button type="warning" style="width: 90%;height: 50px" @click="showabout()">
                    <el-icon><Star /></el-icon>
                    帮助
                </el-button>
            </el-col>
            <el-col :span="6"></el-col>
        </el-row>
    </el-container>
    <router-view></router-view>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "FirstPage",
        setup(){
            let router=useRouter()
            function tohome() {
                router.push('/home/')
            }
            function tologin() {
                router.push('/login/')
            }
            function showabout() {
                router.push('/about')
            }
            return {tohome,tologin,showabout}
        }
    }
</script>

<style scoped>
    .el-row{
        width: 100%;
        margin: 20px auto;
    }
</style>