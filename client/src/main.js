import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faUser, faTimes, faPencilAlt, faPlus} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Multiselect from 'vue-multiselect'
import axios from 'axios'

library.add(faUser, faTimes, faPencilAlt, faPlus);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('multiselect', Multiselect);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.prototype.axios = axios;


Vue.config.productionTip = false;


new Vue({
    router,
    render: h => h(App)
}).$mount('#app');
