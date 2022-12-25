<template>
    <div style="width: 100%;height: 100%;display: flex;flex-direction: column;align-items: center" class="aboutdiv">
        <img src="../assets/about.jpg" style="height: 80%;height: 20%;object-fit: cover;border-radius: 0.05rem">
        <strong style="font-size: 0.3rem;color: #00aea0">进销存管理系统</strong>
        <el-divider>
            <el-icon style="font-size: 0.3rem;color:red">
                <star-filled/>
            </el-icon>
        </el-divider>
        <div style="width: 100%;text-align: center;">
            <el-button @click="gorecmain" style="height: 0.5rem;width: 30%" type="success"><el-icon><Aim /></el-icon>开始</el-button>
            <el-button @click="gohelp" style="height: 0.5rem;width: 30%;margin-left: 0.5rem" type="warning">
                <el-icon><HelpFilled /></el-icon>
                操作指南
            </el-button>
        </div>
    </div>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "About",
        setup(){
            let router=useRouter()
            let gorecmain=()=>{
                router.push('/home/recordacc/recmain/')
            }
            let gohelp=()=>{
                router.push('/home/help/')
            }
            return {gorecmain,gohelp}
        }
    }
</script>

<style scoped>
 .aboutdiv>*{
     margin-top: 0.4rem;
 }
</style>