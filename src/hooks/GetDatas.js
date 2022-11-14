export default {
    gettoken() {
        let xhr=new XMLHttpRequest()
        xhr.open('GET','/django/gettoken/',false)
        xhr.send()
        return xhr.responseText
    },
    getdata() {
        let xhr=new XMLHttpRequest()
        let mid=Math.ceil(Math.random()*15).toString().padStart(3,'0')
        xhr.open('GET',`/django/getdata/?id=${mid}`,false)
        xhr.send()
        return JSON.parse(xhr.responseText)
    },

    postdata() {
        let fd=new FormData()
        fd.append('id',Math.ceil(Math.random()*1000).toString().padStart(3,'0'))
        fd.append('name','Vue测试POST数据')
        fd.append('salary',Math.ceil(Math.random()*100000))
        let xhr=new XMLHttpRequest()
        xhr.open('POST','/django/postdata/',false)
        xhr.setRequestHeader('X-CSRFToken',this.gettoken())
        xhr.send(fd)
        return JSON.parse(xhr.responseText)
    }
}