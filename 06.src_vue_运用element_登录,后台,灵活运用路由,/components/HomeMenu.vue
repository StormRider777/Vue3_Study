<template>
    <el-menu
            active-text-color="#ffd04b"
            background-color="#545c64"
            class="el-menu-vertical-demo"
            default-active="ywsr"
            text-color="#fff"
            @open="handleOpen"
            @close="handleClose"
            @select="selemenu"
            router
    >

        <el-sub-menu index="/home/" >
            <template #title>
                <el-icon style="color: orangered;font-size: 18px">
                    <document/>
                </el-icon>
                <span >业务管理</span>
            </template>

            <el-menu-item index="/home/ywsr">
               <el-icon style="color: blue"><Apple /></el-icon>
                业务输入
            </el-menu-item>
            <el-menu-item index="/home/ywxg">
                <el-icon><Money /></el-icon>
                业务修改
            </el-menu-item>

            <el-menu-item index="/home/ywsh">
                <el-icon style="color: deepskyblue"><Coin /></el-icon>
                业务审核
            </el-menu-item>
            <!--</el-menu-item-group>-->
        </el-sub-menu>
        <el-menu-item index="/home/ywcx">
            <el-icon style="color: red"><Avatar /></el-icon>
            <span>业务查询</span>

        </el-menu-item>
        <el-menu-item index="3" disabled>
            <span>图标不可用</span>
        </el-menu-item>
        <el-sub-menu index="setting">

            <template #title>
                <span>系统设置</span>
            </template>

            <el-menu-item index="">人员设置</el-menu-item>
            <el-menu-item index="">权限设置</el-menu-item>
            <el-menu-item index="">部门设置</el-menu-item>
            <el-menu-item index="">分类编码设置</el-menu-item>
            <el-menu-item index="/home/register">人员注册</el-menu-item>

        </el-sub-menu>
    </el-menu>

</template>

<script>
    import {useRouter} from 'vue-router'
    import {onMounted,ref,watch} from 'vue'
    import {useStore} from 'vuex'

    export default {
        name: "HomeMenu",
        setup() {
            const router = useRouter()
            const path = ref(router.currentRoute.value.path)
            const store=useStore()

            watch(path,(nv,ov)=>{
                // console.log(nv,ov)
            })
            const handleOpen = (key, keyPath) => {
                // console.log(key, keyPath)
            }
            const handleClose = (key, keyPath) => {
                // console.log(key, keyPath)
            }
            onMounted(()=>{
                const router=useRouter()
                store.commit('curpath',router.currentRoute.value.fullPath)
            })

            function selemenu(index,indexpath,item,res) {
                // console.log('1:',index)
                // console.log('2:',indexpath)
                store.commit('curpath',indexpath.slice(-1)[0])
                // console.log('3:',item)
                // console.log('4:',res)
            }
            return {handleOpen,handleClose,selemenu}
        }
    }
</script>

<style scoped>

</style>