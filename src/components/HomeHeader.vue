<template>
    <el-row>
        <el-col :span="22" ><span style="color: red;font-size: 28px;font-weight: bold">业务管理信息系统</span></el-col>
        <el-col :span="2">
            <el-button type="danger" @click="exitos()">
                <el-icon><SwitchButton /></el-icon>
                退出系统
            </el-button>
        </el-col>
    </el-row>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "HomeTitle",
        setup(){
            let  router=useRouter()
            function exitos() {
                router.push('/')
            }
            return{exitos}
        }
    }
</script>

<style scoped>

</style>