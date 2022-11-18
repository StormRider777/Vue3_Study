<template>
    <img alt="Vue logo" src="./assets/logo.png" style="width:60px;height: 60px">
    <MyPage></MyPage>
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
