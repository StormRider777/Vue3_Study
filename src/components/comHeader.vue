<template>
    <div style="display: flex;justify-content: space-between;align-items:center;height: 100%;padding-left: 0.1rem;padding-right: 0.1rem">
        <div style="color:white;font-size: 0.22rem;display: flex;justify-content: center;text-align: left">
            <img src="../assets/logo.png" alt="" style="width: 0.4rem;height: 0.4rem;object-fit: cover" @click="gohome">
            <a href="javascript:void(0)" @click="gohome">进销存记账系统</a>
        </div>
        <div v-text="$store.state.logininfo.account+'  '+$store.state.logininfo.name"
             style="width: 30%;height: 0.25rem;font-size: 0.15rem;line-height: 0.25rem;text-align: right;
             text-overflow:ellipsis; white-space: nowrap;overflow: hidden"></div>
    </div>
</template>

<script>
    import {useRouter} from 'vue-router'
    import {useStore} from 'vuex'
    import {ref} from 'vue'
    export default {
        name: "comHeader",
        setup(){
            let router=useRouter()
            let stroe=useStore()
            let gohome=()=>{
                router.push('/home/')
            }


            return {gohome}
        }
    }
</script>

<style scoped>
    a{
        text-decoration: none;
        color:white;
        display: block;
        margin-left: 0.05rem;
    }
    a:visited{
        color: white;
    }
</style>