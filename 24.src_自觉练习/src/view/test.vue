<template>
    <h2>业务处理页面</h2>
    <hr>
    <div class="testgetpost">
        <el-button type="primary" @click="getdata()">获取一条数据</el-button>
        <div v-text="data.getdata" style="width: 500px;height: 120px;border: 2px double green;
                                    border-radius: 5px;color: yellow;background: #f2e7e5;padding: 10px">
        </div>

        <hr>

        <el-button type="success" @click="postdata()">POST 数据</el-button>
        <div v-text="data.postdata" style="width: 500px;height: 120px;border: 2px double green;
                                    border-radius: 5px;color: yellow;background: #f2e7e5;padding: 10px">
        </div>
    </div>
</template>

<script>
    import {$get,$post} from "../request/request"

    import {reactive} from "vue"
    import {ElMessage} from "element-plus"
    export default {
        name: "home",
        setup(){
            const data=reactive({
                getdata:null,
                postdata:null
            })
            let getdata=()=>{
                $get('/app01/getdata/').then(res=>{
                    ElMessage({message:'Get 发送数据成功!',type:'success',duration:1000})
                    data.getdata=res.data
                }).catch(e=>{
                    data.getdata=e.message
                })
            }
            let postdata=()=>{
                let formdata=new FormData()
                formdata.append('name','Mike')
                formdata.append('pwd',Math.ceil(Math.random()*100000))

                $post('/app01/postdata/',formdata).then(res=>{
                    ElMessage({message:'POST 发送数据成功!',type:'success',duration:1000,'show-close':true})
                    data.postdata=res.data
                }).catch(e=>{
                    data.postdata=e.message
                })
            }
            return {data,getdata,postdata}
        }
    }
</script>

<style scoped>
    .testgetpost{
        height: 400px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
    }
</style>