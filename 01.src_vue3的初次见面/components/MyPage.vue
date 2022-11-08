<template>
    <div>
        <h3>MyPage</h3>
        <hr>
        <p>当前数值:<span v-text="sumbumber"></span></p>
        <button @click="addnumber()">点我看看变化</button>
        <p><button @click="modifydata()">修改值看看,是否反应到页面</button></p>
    </div>
</template>

<script>
    export default {
        name: "MyPage",
        data(){
            return{
                sumbumber:1
            }
        },
        methods:{
            addnumber(){
                this.sumbumber++
                console.log(this)
            },
            modifydata(){
                this.sumbumber=10
                this.$
            }
        },



    }
</script>

<style scoped>

</style>