<template>
    <img alt="Vue logo" src="./assets/logo.png" style="width:60px;height: 60px">
    <MyPage></MyPage>
    <div style="margin:10px auto;width:120px;display: flex;justify-content: space-between;">
        <div style="width:50px;height: 50px;background: aqua;border-radius: 25px"></div>
        <div style="width:50px;height: 50px;background: red;border-radius: 25px"></div>
    </div>
    <pre style="text-align: left;font-size: 16px;">
        与Vue2的不同
        1.vue3的 main.js
            createApp(App).mount('#app')
        2.App.vue 的template 标签内的元素,多元素可以并列

    </pre>
</template>

<script>
import MyPage from "./components/MyPage"

export default {
    name: 'App',
    components: {
     MyPage
    },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
