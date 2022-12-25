<template>
        <h2>Tabs测试</h2>
        <hr>
        <el-button type="success" @click="addonetab">增加一个标签</el-button>
        <el-tabs v-model="activeName"
                 class="demo-tabs"
                 type="card"
                 @tab-click="handleClick"
                 @edit="editTabs">

            <el-tab-pane label="用户" name="tabs_main">
                <!--首个标签页,不可删除-->
                <home></home>
            </el-tab-pane>
            <el-tab-pane v-for="(item,index) in selfdeftabs"
                         :key="index"
                         :name="item.name"
                         :label="item.title"
                         closable>
                <!--动态组件 显示位置.....重要-->
                <component :is="item.content"></component>
            </el-tab-pane>
        </el-tabs>
</template>

<script>
    import {ref,reactive,shallowRef,defineAsyncComponent} from 'vue'
    import home from '../view/home'
    export default {
        name:'MyElTabs',
        components:{
            home
        },

        setup(){
            const activeName = ref('tabs_main')
            const selfdeftabs=ref([])
            const handleClick = (tab, event) => {
                //console.log(tab, event)
            }

            let addonetab=()=>{
                let tabid=selfdeftabs.value.length+1
                let mtab='tab_'+tabid.toString()
                selfdeftabs.value.push({
                    name:mtab,
                    title:'自定义tab-'+tabid.toString(),
                    /**
                     * 重要!!!动态组件
                     */
                    content:shallowRef(defineAsyncComponent(()=>import("../views/test_"+tabid.toString()+".vue")))
                })
                activeName.value=mtab
            }
            let editTabs=(targetName,actions)=>{
                console.log(targetName, actions)
                let tabs=selfdeftabs.value
                if (actions==='remove'){
                    selfdeftabs.value = tabs.filter((tab) => tab.name !== targetName)
                }

            }

            return {activeName,handleClick,addonetab,selfdeftabs,editTabs}
        }
    }
</script>
<style>
    .demo-tabs > .el-tabs__content {
        padding: 32px;
        color: #6b778c;
        font-size: 32px;
        font-weight: 600;
    }
</style>