<template>
    <!--<router-link to="/login/">ssss</router-link>-->
    <router-view></router-view>

</template>

<script>
    import FirstPage from './view/login/FirstPage'
    export default {
        name: "App",
        setup(){},
        components:{
            FirstPage
        }
    }
</script>

<style scoped>


</style>
