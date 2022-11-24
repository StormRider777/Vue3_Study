import {createRouter,createWebHashHistory,createWebHistory} from "vue-router"
import Login from "../view/login/Login"
import Home from "../view/ywgl/Home"
import About from "../view/ywgl/About"
import Register from "../view/login/register"

export default createRouter({
    history:createWebHistory(),
    routes:[
        {
          path:'/',
          name:'firstpage',
          component:()=>import("../view/login/FirstPage.vue")
        },
        {
            path:"/login/",
            name:'login',
            component:Login
        },
        {
            path:"/about/",
            name:'about',
            component:About
        },
        {
            path:'/reg/',
            name:'reg',
            component:Register
        },
        {
            path:'/home/',
            name:'home',
            component:Home,
            children:[
                {
                    path:'ywsr',
                    name:'ywsr',
                    component:()=>import('../view/ywgl/childrens/YwSr.vue'),
                    meta:{
                        title:'业务输入',
                        mymeta:'asdfasfasf'
                    }
                },
                {
                    path:'ywxg',
                    name:'ywxg',
                    component:()=>import('../view/ywgl/childrens/YwXg.vue'),
                    meta:{
                        title:'业务修改'
                    }
                },
                {
                    path:'ywsh',
                    name:'ywsh',
                    component:()=>import('../view/ywgl/childrens/YwSh.vue'),
                    meta:{
                        title:'业务审核'
                    }
                },
                {
                    path:'ywcx',
                    name:'ywcx',
                    component:()=>import('../view/ywgl/childrens/YwCx.vue'),
                    meta:{
                        title:'业务查询'
                    },
                    children: [
                        {
                            path:'ywcxres1',
                            name:'ywcxres1',
                            component:()=>import("../view/ywgl/childrens/YwCxRes")
                        }
                    ]
                },
                {
                    path:'register',
                    name:'register',
                    component:Register
                },
                {
                    path:'ywcxres2',
                    name:'ywcxres2',
                    component:()=>import("../view/ywgl/childrens/YwCxRes")
                }
            ]
        }
    ]
})