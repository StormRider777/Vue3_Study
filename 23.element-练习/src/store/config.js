
export default {
    namespaced:true,
    state:{
        type:'I am moduls of config',
        CurrentUserName:'',
        CurrentUserPwd:'',
        RememberMe:false,
        Token:'',
        CurrentTheme:'Default',
        Exmenu:false,
        MenuThemes:{
            Default:{name:'默认主题',bgcolor:'#545c64'},
            SkyBlue:{name:'天蓝主题',bgcolor:'#1677b3'},
            SeaBlue:{name:'海蓝主题',bgcolor:'#15559a'},
            DeepBlue:{name:'深蓝主题',bgcolor:'#000022'},
            Red:{name:'红色主题',bgcolor:'#c02c38'},
            Green:{name:'绿色主题',bgcolor:'#1a6840'},
            Yellow:{name:'黄色主题',bgcolor:'#e2d849'},
            Gray:{name:'灰色主题', bgcolor:'#363433'},
            Black:{name:'黑色主题',bgcolor:'#000a03'}
        }
    },
    getters:{

    },
    actions:{

    },
    mutations:{
        UpdateUser(state,param){
            state.CurrentUserName=param.name
            state.CurrentUserPwd=param.pwd
            state.RememberMe=param.rememberme
        },
        saveToken(state,param){
            //console.log('param:',param)
            state.Token=param
        },
        Exmenu(state,param){
            state.Exmenu=param
        },
        ChangeTheme(state,param){
            state.CurrentTheme=param
            localStorage.setItem('Theme',param)
        }
    },
}