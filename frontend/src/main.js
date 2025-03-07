import 'vuestic-ui/styles/essential.css'
import './assets/main.css'

import { createApp } from 'vue'
// import { createPinia } from 'pinia'
import { createVuestic } from "vuestic-ui";

import App from './App.vue'
import router from './router'
import "vuestic-ui/css";

const app = createApp(App)

// app.use(createPinia())
app.use(router)
app.use(createVuestic(undefined))
app.mount('#app')
