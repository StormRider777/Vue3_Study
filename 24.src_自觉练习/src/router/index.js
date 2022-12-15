
import {createRouter,createWebHistory} from "vue-router"
import Nprogress from "nprogress"
import "nprogress/nprogress.css"

const router=createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            component:()=>import("../view/index.vue")
        },{
            path:'/about/',
            component:()=>import("../view/about.vue")
        },{
            path:'/home/',
            component:()=>import("../view/home.vue"),
            children:[
                {
                    path:'test',
                    component:()=>import("../view/test.vue")
                }
            ]
        },{
            path:'/login/',
            component:()=>import("../view/login.vue")
        }

    ]
})

router.beforeEach((to,from,next)=>{
    //console.log(to,from)
    Nprogress.start()
    next()
})

router.afterEach((to,from)=>{
    Nprogress.done()
    //console.log(to,from)
})

export default router