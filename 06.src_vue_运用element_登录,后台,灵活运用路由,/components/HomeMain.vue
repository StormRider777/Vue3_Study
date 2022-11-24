<template>
    <span v-text="$store.state.path"></span>
    <hr>
    <router-view></router-view>
</template>

<script>
    import {useStore} from 'vuex'
    import {reactive} from 'vue'
    export default {
        name: "HomeMain",
        setup() {
            let store=reactive(useStore())
            //console.log(store)
        }
    }
</script>

<style scoped>

</style>