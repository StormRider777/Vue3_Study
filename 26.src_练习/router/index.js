import {createWebHistory,createRouter} from 'vue-router'

export default createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            component:()=>import("../view/home.vue")
        },
        {
            path:'/uploadimg/',
            component:()=>import("../view/uploadimg.vue")
        },
        {
            path:'/viewimg',
            component:()=>import("../view/viewimg.vue")
        },
        {
          path:'/explortExcel/',
          component:()=>import("../view/explortExcel.vue")
        },
        {
          path:'/sxr/',
          component:()=>import("../view/sxr.vue")
        },
        {
          path:'/myeltabs/',
          component:()=>import("../view/MyElTabs.vue")
        },



    ]
})