import { createApp } from 'vue'
import App from './App.vue'

import "./assets/style.css"

import Layui from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'

import * as icons from '@element-plus/icons-vue'

import router from "./router/index"
import store from "./store/index"

const app=createApp(App)
app.use(Layui)

app.use(router)
app.use(store)

for (const [key, component] of Object.entries(icons)) {
    app.component(key, component)
}

app.mount('#app')
