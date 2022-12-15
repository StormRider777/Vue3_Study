<template>
    <div style="border: 1px solid lightgrey;width: 92%;margin: 5px auto;
            height: 35px;line-height: 35px;text-align: center;border-radius:5px;color: ghostwhite;height: 35px "
            v-text="$store.state.config.Exmenu?'SDTP':'SDTP 信息管理系统'">
    </div>
    <el-menu
                active-text-color="#ffd04b"
                :background-color="$store.state.config.MenuThemes[$store.state.config.CurrentTheme].bgcolor"
                class="el-menu-vertical-demo"
                default-active="1-1"
                text-color="#fff"
                @open="handleOpen"
                @close="handleClose"
                :collapse="$store.state.config.Exmenu"
        >
            <el-sub-menu index="1">
                <template #title>
                    <el-icon>
                        <location/>
                    </el-icon>
                    <span>Navigator One</span>
                </template>
                <el-menu-item-group title="Group One">
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item two</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="Group Two">
                    <el-menu-item index="1-3">item three</el-menu-item>
                </el-menu-item-group>
                <el-sub-menu index="1-4">
                    <template #title>item four</template>
                    <el-menu-item index="1-4-1">item one</el-menu-item>
                </el-sub-menu>
            </el-sub-menu>
            <el-menu-item index="2">
                <el-icon><StarFilled /></el-icon>
                <span>Navigator Two</span>
            </el-menu-item>
            <el-menu-item index="3" disabled>
                <el-icon>
                    <document/>
                </el-icon>
                <span>Navigator Three</span>
            </el-menu-item>
            <el-menu-item index="4">
                <el-icon>
                    <setting/>
                </el-icon>
                <span>Navigator Four</span>
            </el-menu-item>
        </el-menu>
</template>

<script>
    import {useStore} from 'vuex'
    import {reactive,ref} from 'vue'
    export default {
        name: "MenuV",
        setup(){
            let store=useStore()
            const handleOpen = (key, keyPath) => {
                //console.log(key, keyPath)
            }
            const handleClose = (key, keyPath) => {
                //console.log(key, keyPath)
            }
            return {handleOpen,handleClose}
        }
    }
</script>

<style scoped>
    .el-menu{
        width: 99%;
        border: 0;
        transition: all 0s;
    }
</style>