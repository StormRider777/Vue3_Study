<template>
    <div style="display: flex;justify-content: center;align-items: center;margin: 100px auto">
        <lay-button type="normal" style="height: 45px;width: 250px" @click="gotest()">测试</lay-button>
        <lay-button type="warm" style="height: 45px;width: 250px" @click="goswj()">山东省电子税务局缴纳税款</lay-button>
    </div>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "home",
        setup(){
            const  router=useRouter()
            let gotest=()=>{
                router.push('/test/')
            }
            let goswj=()=>{
                router.push('/sdsw/sbzx-cjpt-web/biz/skjn/qjsk/form/qjsk.html')
            }
            return {gotest,goswj}
        }
    }
</script>

<style scoped>

</style>