<template>
    <div class="common-layout">
        <el-container>
            <el-container>
                <el-aside :width="$store.state.config.Exmenu?'60px':'200px'"
                          :style="{background:$store.state.config.MenuThemes[$store.state.config.CurrentTheme].bgcolor}">
                        <MenuV></MenuV>
                </el-aside>
                <el-container>
                    <el-header
                            :style="{background:$store.state.config.MenuThemes[$store.state.config.CurrentTheme].bgcolor,height:'45px'}">
                        <MenuH></MenuH>
                    </el-header>
                    <el-main>
                        <router-view  v-slot="{ Component }">
                            <transition name="aniview">
                                <component :is="Component" />
                            </transition>
                        </router-view>
                    </el-main>
                </el-container>
            </el-container>
            <el-footer
                    :style="{background:$store.state.config.MenuThemes[$store.state.config.CurrentTheme].bgcolor,height:'40px'}">
                <Footer></Footer>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    import {onBeforeMount,onMounted,reactive} from 'vue'
    import {useStore} from 'vuex'
    import {useRouter} from 'vue-router'
    import MenuH from "../component/MenuH"
    import MenuV from "../component/MenuV"
    import Footer from "../component/Footer"
    export default {
        name: "Home",
        components:{MenuH,MenuV,Footer},
        setup(){
            const store=useStore()
            const router=useRouter()

            const loginuserinfo=reactive({
                username:store.state.config.CurrentUserName,
                userpwd:store.state.config.CurrentUserPwd,
            })
            //console.log(store.state.config)
            onBeforeMount(()=>{
                if  (!loginuserinfo.username || !loginuserinfo.userpwd){
                    router.push('/login/')
                }
            })


            return {}
        }
    }
</script>

<style scoped>
    .common-layout,.el-container {
        width: 100%;
        height: 100%;
    }
    .el-aside{
        overflow-y: auto;
        overflow-x: hidden;
        transition: all 0.5s;
    }
    .el-main{
        overflow: hidden;
    }
    .el-footer{
        overflow: hidden;
        line-height: 40px;
    }
    .aniview-enter-from,.aniview-leave-to{
        position: absolute;
        left: 220px;
        top: 60px;
        transform: translateX(100%);
        opacity: 0;
    }

    .aniview-enter-to,.aniview-leave-from{
        transform: translateX(0px);
        opacity: 1;
    }

    .aniview-enter-active,.aniview-leave-active{
        transition: all 1s ease-in-out;
    }

</style>