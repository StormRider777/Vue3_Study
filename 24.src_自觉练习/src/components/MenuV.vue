<template>

    <el-menu
            active-text-color="#ffd04b"
            :background-color="$store.state.MenuConfig.Themes[$store.state.MenuConfig.CurrentTheme].bgcolor"
            class="el-menu-vertical-demo"
            default-active="2"
            text-color="#fff"
            @open="handleOpen"
            @close="handleClose"
            :collapse="$store.state.MenuConfig.isCollapse"

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
            <el-icon>
                <Edit/>
            </el-icon>
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
    import {useStore} from "vuex"
    import {useRouter} from "vue-router"
    import {reactive,ref} from 'vue'
    export default {
        name: "MenuV",
        setup(){
            const store=useStore()
            const router=useRouter()
            const handleOpen = (key, keyPath) => {
               // console.log(key, keyPath)
            }
            const handleClose = (key, keyPath) => {
                //console.log(key, keyPath)
            }

            return {
                handleClose,
                handleOpen
            }
        }
    }
</script>

<style scoped>
.el-menu,.el-menu>*{
    width: 98%;
    border: 0px;
}
</style>