<template>
    <div>
        <h2>资产情况</h2>
        <table style="width: 300px;margin: 10px auto;border-color: green" border="1" cellpadding="0" cellspacing="0">
            <tr><td><h4 v-text="asset_ldzc"></h4></td><td style="text-align: right"><h4 v-text="asset_ldzc_total"></h4></td></tr>

            <tr><td><h5 v-text="asset_ldzc_mx.xj.title"></h5></td><td style="text-align: right"><h5 v-text="asset_ldzc_mx.xj.total"></h5></td></tr>
            <tr><td><h5 v-text="asset_ldzc_mx.ch.title"></h5></td><td style="text-align: right"><h5 v-text="asset_ldzc_mx.ch.total"></h5></td></tr>


            <tr><td><h4 v-text="asset_gdzc"></h4></td><td style="text-align: right"><h4 v-text="asset_gdzc_total"></h4></td></tr>
            <tr><td><h4 v-text="'合计'"></h4></td><td style="text-align: right"><h4 v-text="asset_total"></h4></td></tr>
            <tr><td colspan="2"><h4><button @click="sumzcze()">点我随机改变,并计算合计值</button></h4></td></tr>
            <tr><td colspan="2">
                <div style="text-align: left">
                <pre>

                import {ref} from "vue"
                export default {
                    name: "MyPage",
                    // vue3 中尽量避免 使用vue2的配置方法
                    // vue2 data(){},methods:{...},computed:{},mounted(),beforecreate(){} beforedestory(){} 都在setup中配置
                    // 响应式数据 使用 vue的 ref函数,转换 实例实现对象  refImpl
                    // setup 可以返回两种数据:
                    // 1.对象类型,2'渲染对象...引入 vue的 h 函数.
                    // 对象数据类型,的应用: ===>   对象类型数据.value.对象的属性='sssss'
                    setup(){
                        var asset_ldzc=ref('流动资产')
                        var asset_ldzc_total=ref(12000)
                        var asset_gdzc=ref('固定资产')
                        var asset_gdzc_total=ref(40000)
                        var asset_total=ref(0)
                        var asset_ldzc_mx=ref({xj:{},ch:{}})


                        function sumzcze() {
                            asset_ldzc_total.value=Math.ceil(Math.random()*1000000)
                            asset_gdzc_total.value=Math.ceil(Math.random()*1000000)
                            asset_ldzc_mx.value.xj={title:'现金',total:Math.ceil(Math.random()*1000000)}
                            asset_ldzc_mx.value.ch={title:'存货',total: asset_ldzc_total.value-asset_ldzc_mx.value.xj.total}


                            asset_total.value=asset_ldzc_total.value+asset_gdzc_total.value
                            console.log(asset_ldzc_mx.value)
                        }
                        return {
                            asset_ldzc,
                            asset_gdzc,
                            asset_gdzc_total,
                            asset_ldzc_total,
                            asset_total,
                            sumzcze
                        }
                    }
                }
            </pre>
            </div></td></tr>
        </table>

    </div>
</template>

<script>
    import {ref} from "vue"
    export default {
        name: "MyPage",
        // vue3 中尽量避免 使用vue2的配置方法
        // vue2 data(){},methods:{...},computed:{},mounted(),beforecreate(){} beforedestory(){} 都在setup中配置
        // 响应式数据 使用 vue的 ref函数,转换 实例实现对象  refImpl
        // setup 可以返回两种数据:
        // 1.对象类型,2'渲染对象...引入 vue的 h 函数.
        setup(){
            var asset_ldzc=ref('流动资产')
            var asset_ldzc_total=ref(12000)
            var asset_gdzc=ref('固定资产')
            var asset_gdzc_total=ref(40000)
            var asset_total=ref(0)
            var asset_ldzc_mx=ref({xj:{},ch:{}})

            function sumzcze() {
                asset_ldzc_total.value=Math.ceil(Math.random()*1000000)
                asset_gdzc_total.value=Math.ceil(Math.random()*1000000)
                asset_ldzc_mx.value.xj={title:'现金',total:Math.ceil(Math.random()*1000000)}
                asset_ldzc_mx.value.ch={title:'存货',total: asset_ldzc_total.value-asset_ldzc_mx.value.xj.total}


                asset_total.value=asset_ldzc_total.value+asset_gdzc_total.value
                console.log(asset_ldzc_mx.value)
            }
            return {
                asset_ldzc,
                asset_gdzc,
                asset_gdzc_total,
                asset_ldzc_total,
                asset_total,
                asset_ldzc_mx,
                sumzcze
            }
        }
    }
</script>

<style scoped>

</style>