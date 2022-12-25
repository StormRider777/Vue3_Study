import md5 from 'md5'

export const  MM=(spwd='')=>{
    return md5(spwd.split('').reverse().join(''))
}

export const  GetStorageUserInfo=()=>{
    let login=localStorage.getItem('logininfo')
    var userinfo={account:'',name:'',pwd:'',autologinck:false}

    if (login){
        login=JSON.parse(login)
        if (login.hasOwnProperty('name')){
            userinfo['account']=login.account
        }
        if (login.hasOwnProperty('pwd')){
            userinfo['pwd']=login.pwd
        }
        if (login.hasOwnProperty('name')){
            userinfo['name']=login.name
        }

        if (login.hasOwnProperty('autologinck')){
            userinfo['autologinck']=login.autologinck
        }
    }
    return userinfo
}
