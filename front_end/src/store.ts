import Vue from 'vue'
import Vuex from 'vuex'
import login from './store/login/index'

Vue.use(Vuex)
export default new Vuex.Store({
  modules: {
    login:login
  }
})
