import {createStore} from 'vuex'

export default createStore({
    state:{
        osinfo:{
            osname: '物业管理信息系统1.0_vuex',
            dwname: '山东欣欣向荣物业有限公司_vuex',
            user:{
                name:'0001',
                pwd:'0000'
            },
            servertoken:'',
            datapath:{
                root:{path:'',title:'根数据服务地址'},
                gettoken:{path:'data/gettoken/',title:'POST数据传输令牌'},
                login:{path:'data/login/',title:'用户登录验证'},
                reguser:{path:'data/reguser/',title:'用户注册'},
                getyzdata:{path:'data/getyzdata/',title:'获取业主数据'},
            }
        }
    },
    actions:{},
    getters:{},
    mutations:{
        updatestate(state,params){
            console.log(params)
        },
        updatetoken(state,params){
            state.osinfo.servertoken=params
        }

    },
})