<template>
    <h2 style="color: blueviolet">业务查询</h2>
    <el-button type="success" style="width: 200px;height: 40px" :icon="Edit" @click="curr_page()">
        <!--<el-icon><Check /></el-icon>-->
        覆盖本页显示结果
    </el-button>
    <el-button type="success" style="width: 200px;height: 40px" :icon="Edit" @click="main_page()">
        <!--<el-icon><Check /></el-icon>-->
        当期页显示查询结果
    </el-button>
        <router-view></router-view>
</template>

<script>
    import {Edit} from "@element-plus/icons-vue"
    import {useRouter} from 'vue-router'
    //import {reactive} from 'vue'
    export default {
        name: "YwCx",
        setup(){
            let router=useRouter()
            function curr_page() {
                router.push('/home/ywcxres2/')
            }
            function main_page() {
                router.push('/home/ywcx/ywcxres1/')
            }
            return{Edit,curr_page,main_page}
        }
    }
</script>

<style scoped>

</style>