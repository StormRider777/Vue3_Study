import {createStore} from 'vuex'

export default createStore({
    state:{
        logininfo:{
            account:'',
            pwd:'',
            name:'',
        }
    },
    getters:{},
    actions:{},
    mutations:{
        ChangeUser(state,value){
            state.logininfo.account=value.account
            state.logininfo.name=value.name
            state.logininfo.pwd=value.pwd
        }
    }
})