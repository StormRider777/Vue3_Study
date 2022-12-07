export default {
    gettoken(url=null,data=null) {
        let xhr=new XMLHttpRequest()
        xhr.open('GET',url,false)
        xhr.send()
        return xhr.responseText
    },
    getdata(url=null,data=null) {
        let xhr=new XMLHttpRequest()
        let mid=Math.ceil(Math.random()*15).toString().padStart(3,'0')
        xhr.open('GET',`${url}?id=${mid}`,true)

        xhr.send()
        return JSON.parse(xhr.responseText)
    },

    postdata(url=null,data=null,token=null) {
        let fd=new FormData()
        fd.append('id',Math.ceil(Math.random()*1000).toString().padStart(3,'0'))
        fd.append('name','Vue测试POST数据')
        fd.append('salary',Math.ceil(Math.random()*100000))
        let xhr=new XMLHttpRequest()
        xhr.open('POST',url,false)
        xhr.setRequestHeader('X-CSRFToken',token)
        xhr.send(fd)
        return JSON.parse(xhr.responseText)
    }
}