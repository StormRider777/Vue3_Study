<template>


    <el-menu active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo" default-active="2" style="width: 200px;border: 0"
             text-color="#fff" @open="handleOpen" @close="handleClose" router :collapse="isCollapse">
        <el-sub-menu index="/home">
            <template #title>
                <el-icon>
                    <location/>
                </el-icon>
                <span>业务管理</span>
            </template>
            <!--<el-menu-item-group title="Group One">-->
            <el-menu-item index="/home/ywgl">业务输入</el-menu-item>
            <el-menu-item index="/home/query">业务查询</el-menu-item>
            <!--</el-menu-item-group>-->
            <!--<el-menu-item-group title="Group Two">-->
                <!--<el-menu-item index="1-3">业务审核</el-menu-item>-->
            <!--</el-menu-item-group>-->
            <el-sub-menu index="'/home">
                <template #title>
                    <el-icon style="color:red">
                        <Delete />
                    </el-icon>
                    <span>业务审核</span>
                </template>
                <el-menu-item index="/home/ywfh">一级审核</el-menu-item>
            </el-sub-menu>
        </el-sub-menu>
    </el-menu>

</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "Menus",
        setup(){
            let isCollapse=ref(false)
            let router=useRouter()
            const handleOpen = (key, keyPath) => {
              //console.log(key, keyPath)
            }
            const handleClose = (key, keyPath) => {
              //console.log(key, keyPath)
            }
            return {handleOpen,handleClose,isCollapse}
        }
    }
</script>

<style scoped>

</style>