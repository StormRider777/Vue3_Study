import {createRouter,createWebHistory} from 'vue-router'

export default createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            name:'FirstPage',
            component:()=>import("../view/login/FirstPage.vue"),
            meta:{
                title:'系统首页入库页面'
            },
            children:[
                {
                    path:'about',
                    name:'about',
                    component:()=>import("../view/About.vue"),
                    meta:{
                        title:'系统帮助功能'
                    }
                }
            ]
        },
        {
            path:'/home/',
            name:'home',
            component:()=>import("../view/home/Home.vue")
        },
        {
            path:'/login/',
            name:'login',
            component:()=>import("../view/login/Login.vue")
        }


    ]
})