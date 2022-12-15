import axios from 'axios'
import Nprogress from 'nprogress'
import "nprogress/nprogress.css"
import {BASE_URL} from './config'

// import {Toast} from 'vant'

const instance=axios.create({
    baseURL: BASE_URL, // 基础请求地址  // process.env.BASE_API  .env.devploment .env.product
    timeout: 10000, // 请求超时设置
    withCredentials: false, // 跨域请求是否需要携带 cookie
});

instance.interceptors.request.use(
    config=>{
        Nprogress.start()
        return config
    },
    error=>{
        Nprogress.done()
        return Promise.reject(error)
    }
)

instance.interceptors.response.use(
    reponse=>{
        Nprogress.done()
        return reponse
    },
    error=>{
        Nprogress.done()
        // Toast({
        //     message: error.message,
        //     duration: 1500,
        //     forbidClick: true
        // });
        return Promise.reject(error)
    }
)

export let $post = function(url, params,token) {

    const query={
        url:url,
        method:'post',
        headers:{
            "Content-Type": 'application/x-www-form-urlencoded;charset=UTF-8',
            'X-CSRFToken':params.csrfmiddlewaretoken,
            //'X-Requested-With':'XMLHttpRequest'
        },
        data:params,
        //data:d,
        //headers:{'Content-Type': 'multipart/form-data'},
        //headers:{'Content-Type': 'application/json;charset=utf-8'}
    }
	return instance(query)
}

export let $get=  function(url,params) {
    const query={
        url:url,
        params:params,
        method:'get',
    }
    return  instance(query)
}
