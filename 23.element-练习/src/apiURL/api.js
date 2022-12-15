import {$get,$post} from "../apiURL/request"

export  function Login(params=null){
    let res= $post("/data/login/",params)
    return res
}
