import axios from 'axios'
import Qs from 'qs'

export default function (name='default_name',pwd='0000',csrf_token='') {
    return new Promise((resolve, reject) => {
        function getcookie (name) {
           var value = '; ' + document.cookie
           var parts = value.split('; ' + name + '=')
           if (parts.length === 2) return parts.pop().split(';').shift()
        }
        let cookie_csrf_token=getcookie('csrftoken')

        let postdata=new FormData()
        postdata.append('name',name)
        postdata.append('pwd',pwd)
        postdata.append('csrfmiddlewaretoken',cookie_csrf_token)//csrf_token)
        // let data= new URLSearchParams()
        // data.append('name',name)
        // data.append('pwd',pwd)
        // data.append('csrfmiddlewaretoken',cookie_csrf_token)
        let data={name:name,pwd:pwd,csrfmiddlewaretoken:cookie_csrf_token}
        //axios.defaults.withCredentials = true
        //axios.defaults.headers.post['Content-Type'] = 'application/json'
        axios({
            //headers: {'Content-Type': 'text/plain;charset=UTF-8'},
            //headers: {'Content-Type': 'application/json;charset=UTF-8','X-CSRFToken': csrf_token},
            //headers:{'X-CSRFToken':csrfmiddlewaretoken,'X-Requested-With':'XMLHttpRequest'},
            headers:{'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','X_CSRFToken':cookie_csrf_token},
            // 'X-CSRFToken': cookie_csrf_token},
            //headers:{'x-csrftoken':cookie_csrf_token},
            //headers:{'X-CSRFToken': cookie_csrf_token},
            //headers:{'X-CSRFToken': csrf_token},
            //headers:{'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','X-CSRFToken': csrf_token},
            //headers:{'X-CSRFToken':cookie_csrf_token,'accessToken':cookie_csrf_token},
            method: 'post',
            url: 'api/postdata/',
            data:postdata,
            xsrfHeaderName:'X-CSRFToken',
            //data:data,
            //data:Qs.stringify(data)
        }).then(res => {
            resolve(res)
        }).catch(err => {
            reject(err)
        })
    })

}

//
//     let dd=''
//     let postdata=new FormData()
//     postdata.append('name',name)
//     postdata.append('pwd',pwd)
//     let data={'name':name,'pwd':pwd}
//     // axios.defaults.baseURL = '/api'
//     axios.get('/api/getdata/')//{name:name,pwd:pwd})
//         .then((res)=>{console.log('res:',res.data);dd=res.data})
//         .catch((err)=>{console.log('err:',err.message);dd=err.message})
//
//     axios({
//         url:'/api/postdata/',
//         method:'post',
//         data:JSON.stringify(data),
//
//         headers:{'Content-Type': 'application/jsonp;charset=utf-8'}
//     })//postdata)
//         .then((res)=>{console.log('res:',res.data);dd=res.data})
//         .catch((err)=>{console.log('err:',err.message);dd=err.message})
// }