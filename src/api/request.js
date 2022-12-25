import axios from 'axios'
import {BASEURL} from './config'
import Nprogress from 'nprogress'
import 'nprogress/nprogress.css'
import {getCookie} from "../../24.src_自觉练习/src/utils/cookiedata";

const request=axios.create({
    baseURL:BASEURL,
    timeout:10000,
    headers:{
        // 'X-CSRFToken':getCookie('csrftoken'),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        //'content-type': 'application/json;charset=utf-8'  //'application/x-www-form-urlencoded',
    }
})

request.interceptors.request.use((config)=>{
    Nprogress.start()
    return config
},((error) => {
    Nprogress.done()
    alert('发生错误:'+error.message)
    return Promise.reject(error.message)
}))

request.interceptors.response.use((reponse)=>{
    Nprogress.done()
    return reponse
},((error) => {
    Nprogress.done()
    alert('发生错误:'+error.message)
    return Promise.reject(error.message)
}))

export const $get=(url=null,params=null)=>{
    return request({
        method:'get',
        url:url,
        params:params
    })
}
export const $post=(url,params)=>{
    return request({
        url:url,
        method:'post',
        data:params,
    }).then(res=>{
        return res.data
    })
}
