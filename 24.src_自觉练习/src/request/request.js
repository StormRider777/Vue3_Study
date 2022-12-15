import axios from "axios"
import {BASE_URL} from "./config";
import Nprogress from "nprogress"
import "nprogress/nprogress.css"
import {getCookie} from "../utils/cookiedata"

const instance=axios.create({
    baseURL:BASE_URL,
    timeout:10000,
    withCredentials: true,
    headers:{
        'X-CSRFToken':getCookie('csrftoken'),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        //'content-type': 'application/json;charset=utf-8'  //'application/x-www-form-urlencoded',
    }
})

instance.interceptors.request.use(config=>{
        Nprogress.start()
        return config
    },error => {
        Nprogress.done()
        return error
})

instance.interceptors.response.use(res=>{
    Nprogress.done()
    return res
},error => {
    Nprogress.done()
    return error
})

export const $get=(url=null,params=null)=>{
    const query={
        url:url,
        params:params,
        method:'get',
    }
    return instance(query)
}
export const $post=(url=null,params=null)=>{
    const query={
        url:url,
        data:params,
        method:'post'
    }
    return instance(query)
}