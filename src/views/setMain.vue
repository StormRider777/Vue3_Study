<template>
    <table style="margin: 0.8rem auto;width: 80%">
        <tr><td><el-button type="primary" @click="goSetUser"><el-icon><User /></el-icon>用户设置</el-button></td></tr>
        <tr><td><el-button type="success" @click="goSetKm"><el-icon><Share /></el-icon>科目设置</el-button></td></tr>
        <tr><td><el-button color="#003003"><el-icon><Setting /></el-icon>系统设置</el-button></td></tr>
    </table>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "setMain",
        setup(){
            let router=useRouter()
            let goSetUser=()=>{
                router.push('/home/user/setuser')
            }
            let goSetKm=()=>{
                router.push('/home/sets/setkm')
            }
            return {goSetUser,goSetKm}
        }
    }
</script>

<style scoped>
    tr{
        height:0.7rem;
    }
    td{
        text-align: center;
    }
    .el-button{
        height: 0.5rem;
        width: 90%;
    }
</style>