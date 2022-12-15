<template>
    <div class="common-layout">
        <el-container>
            <el-aside :width="$store.state.MenuConfig.isCollapse?'60px':'200px'"
                    :style="{'background':$store.state.MenuConfig.Themes[$store.state.MenuConfig.CurrentTheme].bgcolor}">
                <MenuV></MenuV>
            </el-aside>
            <el-container>
                <el-header :style="{'background':$store.state.MenuConfig.Themes[$store.state.MenuConfig.CurrentTheme].bgcolor}">
                    <MenuH></MenuH>
                </el-header>
                <el-main>
                    <router-view></router-view>
                </el-main>
                <el-footer :style="{'background':$store.state.MenuConfig.Themes[$store.state.MenuConfig.CurrentTheme].bgcolor}">Footer</el-footer>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    import {onMounted} from "vue"
    import {useRouter} from 'vue-router'
    import MenuV from "../components/MenuV"
    import MenuH from "../components/MenuH"
    export default {
        name: "home",
        components:{MenuV,MenuH},
        setup(){
            const router=useRouter()
            onMounted(()=>{
               router.push('/home/test')
            })
        }
    }
</script>

<style scoped>
.el-container {
    width: 100%;
    height: 100%;
}
    .el-aside{
        transition: width 0.5s;
    }
    .el-footer{
        height: 40px;
    }
</style>