import {createRouter,createWebHistory} from 'vue-router'
import Nprogress from 'nprogress'
import 'nprogress/nprogress.css' // Progress 进度条样式

import Login from "../view/Login"
import Home from "../view/Home"
import Error from "../view/Error"

const router=createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            redirect:'/login'
        },
        {
            path:'/login/',
            name:'login',
            component:Login
        },
        {
            path:'/home/',
            name:'home',
            component:Home,
            children:[
                {
                    path:'',
                    component:()=>import("../component/HomeMain.vue")
                },
                {
                    path:'error',
                    component:Error
                },
                {
                    path:'my/changpwd',
                    component:()=>import("../view/My/ChangPwd.vue"),
                },
                {
                    path:'my/info',
                    component:()=>import("../view/My/Info.vue"),
                },
                {
                    path:'my/editinfo',
                    component:()=>import("../view/My/EditInfo.vue"),
                }
            ]
        },
        {
            path:'/error/',
            component:Error
        }
    ]
})

router.beforeEach((to,from,next)=>{
    Nprogress.start()
    //console.log("from:",from ,"to:",to)

    next()
})
router.afterEach((to,from)=>{
    Nprogress.done()
})

export default router