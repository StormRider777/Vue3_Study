import {createWebHistory,createRouter} from 'vue-router'

export default createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/sdsw/sbzx-cjpt-web/biz/skjn/qjsk/form/qjsk.html',
            component:()=>import("../view/index.vue")
        },
        {
            path:'/',
            component:()=>import("../view/home.vue"),
        },
        {
            path:'/test/',
            component:()=>import("../view/LayuiTable.vue")
        }


    ]
})