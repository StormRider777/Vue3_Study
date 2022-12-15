import {createStore} from 'vuex'

export default createStore({
    state:{
        MenuConfig:{
            isCollapse:false,
            CurrentTheme:'Default',
            Themes:{
                'Default':{name:'默认主题',bgcolor:'#141e1b'},
                'Red':{name:'红色主题',bgcolor:'#ec2b24'},
                'Green':{name:'绿色主题',bgcolor:'#12a182'},
                'Black':{name:'黑色主题',bgcolor:'#000'},
                'Blue':{name:'钢蓝主题',bgcolor:'#0f1423'},
            }
        }
    },
    actions:{},
    getters:{},
    mutations:{
        ZdMenu(state,value){
            state.MenuConfig.isCollapse=value
        },
        SetTheme(state,value){
            state.MenuConfig.CurrentTheme=value
        }
    },
})