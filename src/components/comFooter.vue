<template>
    <el-menu
            :default-active="activeIndex"
            mode="horizontal"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
            @select="handleSelect"
            :ellipsis="false"
    >
        <el-menu-item index="YwHome" style="width: 25%" @click="goJz">
            <span style="width: 100%;font-size: 0.17rem;text-align: center" >
                业务
                <el-icon><HomeFilled /></el-icon>
            </span>
        </el-menu-item>
        <el-sub-menu index="Querys" style="width: 25%">
            <template #title>
                <span style="font-size: 0.17rem;width: 100%;text-align: center">查询</span>
            </template>
             <el-menu-item index="QueryMain"><el-icon><House /></el-icon>查询总览</el-menu-item>
             <el-menu-item index="dv1" disabled><el-divider border-style="solid" /></el-menu-item>
             <el-menu-item index="QueryYwPage"><el-icon><DocumentCopy /></el-icon>查询业务</el-menu-item>
             <el-menu-item index="QueryUserPage"><el-icon><StarFilled /></el-icon>查询用户</el-menu-item>
             <el-menu-item index="QueryLoginPage"><el-icon><Finished /></el-icon>查询登录日志</el-menu-item>
        </el-sub-menu>
         <el-sub-menu index="Sets" style="width: 25%">
             <template #title>
                 <span style="font-size: 0.17rem;width: 100%;text-align: center">设置</span>
             </template>
             <el-menu-item index="setMain" @click="goSetMain"><el-icon><House /></el-icon>设置总览</el-menu-item>
             <el-menu-item index="dv1" disabled><el-divider border-style="solid" /></el-menu-item>
             <el-menu-item index="setUser" @click="goSetUser"><el-icon><User /></el-icon>用户设置</el-menu-item>
             <el-menu-item index="setKm" @click="goSetKm"><el-icon><Share /></el-icon>科目设置</el-menu-item>
             <el-menu-item index="setSys"><el-icon><Setting /></el-icon>系统设置</el-menu-item>
         </el-sub-menu>
        <el-menu-item index="4" style="width: 25%" @click="goMyInfo">
                <span style="font-size: 0.17rem;width: 100%;text-align: center">
                    我的<el-icon><UserFilled /></el-icon>
                </span>
        </el-menu-item>
    </el-menu>
</template>

<script>
    import {useRouter} from "vue-router"
    import {ref} from 'vue'
    export default {
        name: "comFooter",
        setup(){
            let router=useRouter()
            const activeIndex = ref('1')
            const handleSelect = (key, keyPath) => {
              //console.log(key, keyPath)
            }

            let goMyInfo=()=>{
                router.push('/home/user/myinfo')
            }
            let goJz=()=>{
                router.push('/home/recordacc/RecMain')
            }
            let goSetUser=()=>{
                router.push('/home/user/setuser')
            }
            let goSetMain=()=>{
                router.push('/home/setmain')
            }
            let goSetKm=()=>{
                router.push('/home/sets/setkm')
            }
            return {goMyInfo,goJz,handleSelect,activeIndex,goSetMain,goSetUser,goSetKm}
        }
    }
</script>

<style>
    .el-menu-item {
        font-size: .16rem;
    }
</style>