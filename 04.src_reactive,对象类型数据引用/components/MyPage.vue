<template>
    <div>
        <h2><span v-text="person.name" style="color: red"></span><span>的情况</span></h2>
        <table style="width: 1000px;margin: 10px auto;border-color: green;border-collapse: collapse;" border="1" cellpadding="0" cellspacing="0">
            <tr><td>年龄:</td><td><span v-text="person.age" style="margin-right: 20px"></span>修改: <input type="text" v-model="person.age"> </td></tr>
            <tr><td>喜好:</td><td>
                <span v-for="(h,i) in person.hobby" :key="i">
                    <span v-text="(i+1).toString()+'.'+h" style="margin-left: 10px"></span>
                </span>
            </td></tr>
            <tr><td colspan="2" style="color: red;text-align: left;background: skyblue"><h4>工作情况:</h4></td></tr>
            <tr><td><span>工作单位:</span></td><td><span v-text="person.work.dwmc"></span></td></tr>
            <tr><td><span>职务:</span></td><td><span v-text="person.work.zw"></span></td></tr>
            <tr><td><span>薪酬:</span></td><td><span v-text="person.work.salary"></span></td></tr>
            <tr><td colspan="2" style="color: red;text-align: left;background: skyblue"><h4>拥有的女人:</h4></td></tr>
            <tr><td colspan="2">
                <table style="width:80%;margin: 0 auto;border-style: dot-dash;border-color: gray;margin-top: 10px;margin-bottom: 10px;border-collapse:collapse" border="1" cellpadding="0" cellspacing="0">
                    <thead>
                        <tr style="background: darkgray"><td style="width: 300px;">编号</td><td>姓名</td><td>芳龄</td></tr>
                    </thead>
                    <tr v-for="w in person.wife" :key="w.id">
                        <td><span v-text="w.id"></span></td>
                        <td><span v-text="w.name"></span></td>
                        <td><span v-text="w.age"></span></td>
                    </tr>
                </table>
            </td></tr>
            <tr><td colspan="2"><button @click="sumzcze()" style="height: 25px">点我随机改变,并计算wife的年龄合计值</button></td></tr>
            <tr><td colspan="2">
                <div style="text-align: left">

            </div></td></tr>
        </table>

    </div>
</template>

<script>
    import {reactive} from "vue"
    import {nanoid} from "nanoid"
    export default {
        name: "MyPage",
        // vue3 中尽量避免 使用vue2的配置方法
        // vue2 data(){},methods:{...},computed:{},mounted(),beforecreate(){} beforedestory(){} 都在setup中配置
        // 响应式数据 使用 vue的 ref函数,转换 实例实现对象  refImpl
        // setup 可以返回两种数据:
        // 1.对象类型,2'渲染对象...引入 vue的 h 函数.
        // 尽可能的 数据对象化 ,reactive({})转换成代理对象,进行响应式数据操作
        setup(){
            var person=reactive({
                name:'张三',
                age:25,
                hobby:['抽烟','喝酒','烫头','足球'],
                work:{
                    dwmc:'Django软件集成公司',
                    zw:'Django开发工程师',
                    salary:15000,
                },
                wife:[
                    {id:nanoid(),name:'西施',age:22},
                    {id:nanoid(),name:'貂蝉',age:25},
                    {id:nanoid(),name:'武媚娘',age:26},
                    {id:nanoid(),name:'林黛玉',age:28},
                ],
            })

            function sumzcze() {
                 person.wife[1].name='修改了貂蝉'
            }
            console.log(person)
            return {
                person,
                sumzcze
            }
        }
    }
</script>

<style scoped>
    tr{
        height: 35px;
    }
    td{
        padding-left: 10px;
    }

</style>