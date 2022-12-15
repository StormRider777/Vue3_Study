<template>
    <div style="display: flex;justify-content: space-between">
        <div style="color: ghostwhite;font-size: 35px">
            <div v-show="exmenu" style="display: block"><a href="javascript:void(0)" @click="Expandmenu()"><el-icon><Expand /></el-icon></a></div>
            <div v-show="!exmenu" style="display: block"><a href="javascript:void(0)" @click="Expandmenu()"><el-icon><Fold  /></el-icon></a></div>
        </div>
        <div style="width: 550px">
            <el-menu
                default-active="111"
                class="el-menu-demo"
                mode="horizontal"
                :background-color="$store.state.config.C.bgcolor"
                text-color="#fff"
                active-text-color="#ffd04b"
                @select="handleSelect"
                >
                <el-menu-item index="Home">
                    <el-icon><HomeFilled /></el-icon>
                    首页
                </el-menu-item>
                <el-menu-item index="Query">
                    <el-icon><Search /></el-icon>
                    信息查询
                </el-menu-item>
                <el-sub-menu index="Theme">
                    <template #title>
                        <el-icon><Platform /></el-icon>
                        主题
                    </template>
                    <el-menu-item v-for="k in theme" :index="k">

                        <span v-text="$store.state.config.MenuThemes[k].name">
                        </span>
                        <el-icon v-show="k===$store.state.config.CurrentTheme" style="color:ghostwhite"><Select /></el-icon>
                    </el-menu-item>
                    <!--<el-menu-item index="Default">默认主题</el-menu-item>-->
                    <!--<el-menu-item index="Red">红色主题</el-menu-item>-->
                    <!--<el-menu-item index="Blue">蓝色主题</el-menu-item>-->
                    <!--<el-menu-item index="Green">绿色主题</el-menu-item>-->
                    <!--<el-menu-item index="Yellow">黄色主题</el-menu-item>-->
                    <!--<el-menu-item index="Black">黑色主题</el-menu-item>-->
                    <!--<el-menu-item index="Gray">灰色主题</el-menu-item>-->
                </el-sub-menu>

                <el-sub-menu index="My">
                    <template #title>
                        <el-icon><Avatar /></el-icon>
                        <span v-text="$store.state.config.CurrentUserName"></span>
                    </template>
                    <el-menu-item index="info">我的详情</el-menu-item>
                    <el-menu-item index="editinfo">信息修改</el-menu-item>
                    <el-menu-item index="changpwd">修改密码</el-menu-item>
                    <el-menu-item disabled> <el-divider /></el-menu-item>
                    <el-menu-item index="Exit">系统退出</el-menu-item>
                </el-sub-menu>
            </el-menu>
        </div>
    </div>
</template>

<script>
    import {useStore} from 'vuex'
    import {reactive,ref,onMounted} from 'vue'
    import {useRouter} from 'vue-router'
    export default {
        name: "MenuH",
        setup(){
            let store=useStore()
            let theme=reactive(Object.keys(store.state.config.MenuThemes))
            let router=useRouter()
            const exmenu=ref(store.state.config.Exmenu)
            const activeIndex = ref('1')

            const handleSelect = (key, keyPath) => {
                //console.log(key, keyPath,keyPath[0])
                if (keyPath[0]==='Theme'){
                    store.commit('config/ChangeTheme',key)
                    //theme.bgcolor=store.state.config.MenuThemes[store.state.config.CurrentTheme].bgcolor
                }else if (keyPath[0]==='Home'){
                    router.push('/home/')
                }else if (keyPath[0]==='Query'){
                    router.push('/home/error')
                }else if (keyPath[0]==='My'){
                    let cmd=keyPath[1]
                    if (cmd==='Exit'){
                        store.commit('config/UpdateUser',{name:'',pwd:'',rememberme:''})
                        localStorage.clear()
                        router.push('/')
                    }else{
                        let r='/home/my/'+cmd
                        router.push(r)
                    }
                }
            }
            const Expandmenu=()=>{
                exmenu.value=!exmenu.value
                store.commit('config/Exmenu',exmenu.value)
            }
            return{theme,activeIndex,handleSelect,exmenu,Expandmenu}
        }
    }
</script>

<style scoped>
    .el-menu{
        height: 43px;
        border: 0;
    }
    a{
        text-decoration: none;
        color: ghostwhite;
    }
    a:visited{
        color: ghostwhite;
    }

</style>