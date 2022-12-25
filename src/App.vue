<template>

    <router-view></router-view>
</template>

<script>
    import {onMounted,ref} from 'vue'
    import {useStore} from'vuex'
    import {GetStorageUserInfo} from "./utils/MyUtils"
    export default {
        name:'App',
        setup(){
            let store=useStore()
            onMounted(()=>{
                let login=GetStorageUserInfo()
                store.commit('ChangeUser',{account:login.account,name:login.name,pwd:login.pwd})

            })
        }
    }
</script>

<style scoped>
:deep(.el-input.is-disabled .el-input__inner){
  -webkit-text-fill-color: blue;
}
</style>
