import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vuex from 'vuex'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(Vuex)

router.beforeEach((to, from, next) => {
  if (localStorage.getItem('token')) {
    store.dispatch('menu/GET_USER_INFO')
  }
  if (to.meta.requireAuth) {
    if (localStorage.getItem('token')) {
      next()
    } else {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    }
  } else {
    next()
  }
  if (
    to.path.split('/')[to.path.split('/').length - 1] === 'login' ||
    to.path.split('/')[to.path.split('/').length - 1] === 'register'
  ) {
    if (localStorage.getItem('token')) {
      router.push({
        path: '/'
      })
      location.reload()
    }
  }
})
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
