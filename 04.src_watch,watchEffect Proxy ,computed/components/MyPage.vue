<template>
    <div>
        <span v-text="data"></span>
        <hr>
        <h4 v-text="name"></h4>
        <h4 v-text="age"></h4>
        <h4 v-show="data.sex" v-text="data.sex"></h4>
        <button @click="name+='~'">修改姓名</button>
        <button @click="age++">修改年龄</button>
        <button @click="data.sex='男'">增加性别</button>
        <button @click="delete data.sex">删除性别</button>

    </div>
</template>

<script>
    import {reactive,toRefs,watchEffect} from 'vue'
    export default {
        name: "MyPage",

        setup(){

            const data=reactive({
                name:'东方不败',
                age:30,
            })


            // watchEffect(()=>{
            //     var name=data
            //     console.log('watceffect调用了 ',name)
            // })

            // var row=new Proxy(data,{
            //     get(t,p){
            //         console.log('get:',t,p)
            //         return Reflect.get(t,p)
            //     },
            //     set(t,p,v){
            //         console.log('set:',t,p,v)
            //         return Reflect.set(t,p,v)
            //     }
            // })
            // row.name='adsaf'
            // console.log('row:',row.name)
            // watch(dataTest,(nv, ov)=>{
            //     console.log(nv,ov)
            // })
            //
            // watch(()=>dataTest.name,(nv, ov)=>{
            //     console.log(nv,ov)
            // })
            return {data,...toRefs(data)}
        }

    }
</script>

<style scoped>

</style>