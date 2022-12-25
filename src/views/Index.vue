<template>
        <div style="margin: 0.5rem auto;text-align: center" >
        <el-button @click="gohome">点击进入</el-button>
    </div>

</template>

<script>
    import {useRouter} from "vue-router"
    export default {
        name: "Index",
        setup(){
            let router=useRouter()
            let gohome=()=>{
                router.push('/home/')
            }
            return {gohome}
        }
    }
</script>

<style scoped>

</style>