import { createApp } from 'vue'
import App from './App.vue'

import "./assets/style.css"
import Element from 'element-plus'
import "element-plus/dist/index.css"
import * as icons from '@element-plus/icons-vue'

import router from "./router/index"
import store from "./store/index"

const app=createApp(App)


app.use(router)
app.use(store)
app.use(Element)
for (const [key, component] of Object.entries(icons)) {
    app.component(key, component)
}

app.mount('#app')
