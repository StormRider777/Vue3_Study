<template>
    <div style="width: 500px;margin: 10px auto;border: 1px solid grey;padding: 10px 10px 10px 10px ">
        <span><el-button @click="goback()">
            <el-icon><ArrowLeftBold /></el-icon>
            返回
        </el-button></span>
        <hr>
        <h3 style="color: blue">业务查询结果是:</h3>
    </div>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "YwCxRes",
        setup(){
            let router=useRouter()
            function goback() {
                router.go(-1)
            }
            return {goback}
        }
    }
</script>

<style scoped>

</style>