import {createStore} from 'vuex'
export default createStore({
    state:{
        path:''
    },
    getters:{

    },
    mutations:{
        curpath(state,param){
            state.path=param
        }
    },
    actions:{

    }
})