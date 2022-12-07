import {createStore} from 'vuex'
import config from '../store/config'
import Menus from "../store/menus"
export default createStore({
    state:{},
    getters:{},
    actions:{},
    mutations:{},
    modules:{config,Menus}
})

