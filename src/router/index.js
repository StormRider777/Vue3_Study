import {createWebHistory,createRouter} from 'vue-router'
import Nprogress from "nprogress"
import "nprogress/nprogress.css"

const routers = [
    {
        path:"/",
        component: () => import("../views/Index.vue")
    },
    {
        path: '/login/',
        component: () => import("../views/Login.vue")
    },
    {
        path: '/home/',
        component: () => import("../views/Home.vue"),
        children: [
            {
              path:'',
              component:()=>import('../views/About.vue')
            },
            {
                path: 'user',
                children: [
                    {path: 'myinfo', component: () => import("../views/ManUsers/MyInfo.vue")},
                    {path: 'setuser', component: () => import("../views/ManUsers/QueryUsers.vue")},
                ]
            },
            {
                path: 'setmain',
                component:()=>import("../views/setMain.vue")
            },
            {
                path:'sets',
                children:[
                    {
                        path: 'setkm',
                        component:()=>import("../views/Sets/SetKm.vue")
                    }
                ]
            },
            {
                path: 'help',
                component:()=>import("../views/Help.vue")
            },
            {
                path: 'recordacc',
                children: [
                    {path: 'recmain', component: () => import("../views/JzYw/RecMain.vue")},
                    {path: 'buygoods', component: () => import("../views/JzYw/BuyGoods.vue")},
                ]
            },
        ]
    },
]

const router=createRouter({
    history:createWebHistory(),
    routes:routers
})
router.beforeEach((to,from,next)=>{
    Nprogress.start()
    next()
})
router.afterEach((to,from)=>{
    Nprogress.done()
})
export default router