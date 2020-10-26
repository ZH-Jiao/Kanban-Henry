import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import './assets/formulate.css'
import VueFormulate from '@braid/vue-formulate'


Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueFormulate)

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')