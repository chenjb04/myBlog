import Vue from 'vue'
import Vuex from 'vuex'
import login from './store/login/index'
import register from './store/register/index'
import menu from './store/menu/index'

Vue.use(Vuex)
export default new Vuex.Store({
  modules: {
    login: login,
    register: register,
    menu: menu
  }
})
