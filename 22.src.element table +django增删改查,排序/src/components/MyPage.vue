<template>
    <div>

        <div class="reqtype">
            <button @click="getdata">向 Django-server GET请求一条数据</button>
            <h4 v-text="data.token"></h4>
            <hr>
            <div id="getres" v-text="data.getres"
                 style="line-height:27px;text-align: left;padding:5px 5px 5px 5px;overflow:auto;font-size:16px;color:yellow;border-radius:10px;width:80%;margin: 10px auto;height: 100px;background:#030303">

            </div>
        </div>
        <hr>
        <div class="reqtype">
            <button @click="postdata">向 Django-server POST一条数据</button>
            <hr>
            <div id="getpost" v-text="data.postres"
                 style="line-height:27px;text-align: left;padding:5px 5px 5px 5px;
                 overflow:auto;font-size:16px;color:yellow;border-radius:10px;
                 width:80%;margin: 10px auto;height: 100px;background:#131313">
            </div>
        </div>
    </div>
</template>

<script>
    import Getdatas from '../hooks/GetDatas'
    import {reactive} from 'vue'
    export default {
        name: "MyPage",
        setup(){
            let data=reactive({})

            function getdata(){
                data.getres=Getdatas.getdata()
            }
            function postdata(){
                data.postres=Getdatas.postdata()
            }

            return {data,getdata,postdata}
        }
    }
</script>

<style scoped>
    .reqtype{
        width:60%;
        margin: 10px auto;
        background: blanchedalmond;
        border-radius:5px;
        text-align: center;
        padding-bottom: 10px;
        padding-top: 10px;
    }

    button{
        height: 38px;
        width: 300px
    }
</style>