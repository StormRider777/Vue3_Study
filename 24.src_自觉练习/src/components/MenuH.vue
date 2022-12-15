<template>
    <div class="title">
        <div class="colspan">
            <a href="javascript:void(0)" class="zda" @click="zdiconfunc()" v-show="zdicon"><el-icon><Expand /></el-icon></a>
            <a href="javascript:void(0)" class="zda" @click="zdiconfunc()" v-show="!zdicon"><el-icon><Fold /></el-icon></a>
        </div>
        <div class="MenuHdiv">
            <el-menu
                    :default-active="'1'"
                    class="el-menu-demo"
                    mode="horizontal"
                    :background-color="$store.state.MenuConfig.Themes[$store.state.MenuConfig.CurrentTheme].bgcolor"
                    text-color="#fff"
                    active-text-color="#ffd04b"
                    @select="handleSelect"
            >
                <el-menu-item index="1">主页</el-menu-item>
                <el-sub-menu index="Theme">
                    <template #title>主题</template>

                    <!--<el-menu-item v-for=" item in $store.  " index="2-1">item one</el-menu-item>-->
                    <el-menu-item v-for="item in Object.keys($store.state.MenuConfig.Themes)"
                                  :index="item"
                                  v-text="$store.state.MenuConfig.Themes[item].name">
                    </el-menu-item>
                    <!--<el-menu-item index="2-2">item two</el-menu-item>-->
                    <!--<el-menu-item index="2-3">item three</el-menu-item>-->
                </el-sub-menu>

                <el-sub-menu index="3">
                    <template #title>个人中心</template>
                    <el-menu-item index="3-1">我的详情</el-menu-item>
                    <el-menu-item index="3-2">修改密码</el-menu-item>
                    <el-menu-item index="3-3">退出系统</el-menu-item>
                </el-sub-menu>
            </el-menu>

        </div>
    </div>
</template>

<script>
    import {useStore} from 'vuex'
    import {ref} from 'vue'
    export default {
        name: "MenuH",
        setup(){
            const store=useStore()
            const zdicon=ref(false)
            const handleSelect = (key, keyPath) => {
                //console.log(key, keyPath)
                if (keyPath[0]==='Theme'){
                    store.commit('SetTheme',keyPath[1])
                }
            }
            let zdiconfunc=()=>{
                zdicon.value=!zdicon.value
                store.commit('ZdMenu',zdicon.value)
            }
            return {
                zdicon,
                handleSelect,
                zdiconfunc
            }
        }

    }
</script>

<style scoped>
    .zda{
        text-decoration: none;
        display: block;
        color:red
    }
    .zda:visited{
        color: red;
    }
    .el-menu{
        height: 98%;
        border: 0px;
    }
    .title{
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .MenuHdiv{
        width: 400px;
    }
    .colspan{
        font-size: 30px;
        color: red;
    }
</style>