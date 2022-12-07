<template>

    <router-view></router-view>

</template>

<script>
    import {onMounted} from 'vue'
    import {useStore} from 'vuex'
    import {useRouter} from 'vue-router'
    import {$get} from './apiURL/request'
    import {ElMessageBox,ElMessage} from "element-plus"
    import {Login} from "./apiURL/api"
    export default {
        name: "App",
        setup(){
            const store=useStore()
            const router=useRouter()

            onMounted(()=>{
                $get('/data/gettoken/').then(r=>{
                    clearAllCookie()
                    store.commit('config/saveToken',r.data)
                    setCookie('csrftoken',r.data)

                    let userinfo=localStorage.getItem('loginuserinfo')

                    if (userinfo){
                        let loginuser=JSON.parse(userinfo)
                        if (loginuser.hasOwnProperty('name') && loginuser.hasOwnProperty('pwd') && loginuser.hasOwnProperty('rememberme')) {
                            //console.log(loginuser.rememberme)
                            if (loginuser.rememberme){
                                Login({name:loginuser.name,pwd:loginuser.pwd,csrfmiddlewaretoken:store.state.config.Token}).then(r=>{
                                    if (r.data.res){
                                        let user={name:loginuser.name,pwd:loginuser.pwd,rememberme:loginuser.rememberme}
                                        ElMessage({message:'自动登录成功!'+r.data.result.name,type:'success'})
                                        //store.commit('config/saveToken',r.data)
                                        store.commit('config/UpdateUser',user)
                                        localStorage.setItem('loginuserinfo',JSON.stringify(user))
                                        //let curpath=router.currentRoute.value.fullPath
                                        router.push('/home/')
                                    }else{
                                        ElMessageBox({
                                            message:'自动登录失败:'+r.data.msg,
                                            title:'登录失败',
                                            type:'error'
                                        })
                                        router.push('/login/')
                                    }
                                }).catch(e=>{
                                    ElMessageBox({
                                        message:'失败:'+e.message,
                                        title:'提示',
                                        type:'warning'
                                    })
                                    router.push('/login/')
                                })
                            }
                        }
                    }
                }).catch(e=>{
                    store.commit('config/saveToken','')
                })

                let theme=localStorage.getItem('Theme')
                //console.log(theme,Object.keys(store.state.config.MenuThemes))
                let mn=Object.keys(store.state.config.MenuThemes).indexOf(theme)
                if (mn>=0){
                    store.commit('config/ChangeTheme',theme)
                }else{
                    console.log('fff:',theme)
                    store.commit('config/ChangeTheme','Default')
                }
            })
        }
    }
    function clearAllCookie() {
		var keys = document.cookie.match(/[^ =;]+(?==)/g);
		if(keys) {
			for(var i = keys.length; i--;)
				document.cookie = keys[i] + '=0;expires=' + new Date(0).toUTCString()
		}
	}

    function setCookie(key, value,exdays=30) {
        //校验Key, key中不能有等号【=】
        if(key.indexOf("=") !== -1) {
            throw new Error("Cookie不支持key中使用等号【=】, key:" + key)
        }
        let exdate = new Date() // 获取时间
        exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * exdays) // 保存的天数
        // 字符串拼接cookie
        // eslint-disable-next-line camelcase
        window.document.cookie = key + '=' + value + ';path=/;expires=' + exdate.toGMTString()
    }
    function getCookie(key) {
        if (document.cookie.length > 0) {
            // 这里显示的格式需要切割一下自己可输出看下
            var arr = document.cookie.split('; ')
            for (let i = 0; i < arr.length; i++) {
                let arr2 = arr[i].split('=') // 再次切割
                // 判断查找相对应的值
                if (arr2[0] === key) {
                    var value = arr2[1];
                    for (let j = 2; j < arr2.length; j++) {
                        value += '=' + arr2[j];
                    }
                    return value;
                }
            }
        }
    }


</script>

<style scoped>

</style>
